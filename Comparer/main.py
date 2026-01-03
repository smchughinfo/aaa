import argparse
import open_ai
import json
from pathlib import Path
from EXPERIMENTAL_SYSTEM_PROMPTS import *
from EXPERIMENTAL_TEST_DATA import *
from database import Database
import logging
import config
import asyncio

def get_batches(data_list, batch_size):
    """
    Split a list into batches of specified size.

    Args:
        data_list: The list to split into batches
        batch_size: Number of items per batch

    Returns:
        List of batches (each batch is a list)
    """
    batches = []
    for i in range(0, len(data_list), batch_size):
        batches.append(data_list[i:i + batch_size])
    return batches

def format_output(comparisons, data_answers_batched):
    # Flatten data_answers from batched structure
    data_answers_flat = []
    for batch in data_answers_batched:
        data_answers_flat.extend(batch)

    # Combine comparisons with answers
    formatted_results = []
    for i, comparison in enumerate(comparisons):
        correct_answer = data_answers_flat[i] if i < len(data_answers_flat) else None
        categorized_correctly = comparison.arbitrage_match == correct_answer if correct_answer is not None else None

        formatted_results.append({
            "market_id1": comparison.market_id1,
            "market_id2": comparison.market_id2,
            "relationship": comparison.relationship,
            "arbitrage_match": comparison.arbitrage_match,
            "notes": comparison.notes,
            "correct_answer": correct_answer,
            "categorized_correctly": categorized_correctly
        })

    return formatted_results

def save_results(prompt_num, data_num, data_limit, batch_size, data_answers, results, metadata=None):
    # Combine all batch results into one list
    all_comparisons = []
    for batch_result in results:
        all_comparisons.extend(batch_result.comparisons)

    # Save to database when running in production mode
    if not config.on_dev and metadata is not None:
        # Recombine LLM results with metadata and save to database
        with Database() as db:
            for i, comparison in enumerate(all_comparisons):
                if i >= len(metadata):
                    logging.warning(f"Metadata missing for comparison index {i}, skipping")
                    continue

                meta = metadata[i]

                # Map relationship to comparable bool
                relationship = comparison.relationship
                if relationship in ("EQUIVALENT", "NEGATION"):
                    comparable = True
                elif relationship == "UNCERTAIN":
                    comparable = None
                else:  # SUBSET, SUPERSET, OVERLAP, UNRELATED
                    comparable = False

                db.upsert_comparison(
                    market_1_id=meta['market_1_id'],
                    market_2_id=meta['market_2_id'],
                    market_1_canonical_similarity=meta['market_1_canonical_similarity'],
                    market_2_canonical_similarity=meta['market_2_canonical_similarity'],
                    comparable=comparable
                )

        logging.info(f"Saved {len(all_comparisons)} comparisons to database")

    # Save to files when running in dev mode
    elif config.on_dev:
        output_dir = Path("EXPERIMENTAL_RESULTS")
        output_dir.mkdir(exist_ok=True)  # Create dir if doesn't exist
        output_file = output_dir / f"{prompt_num}_{data_num}_{data_limit}_{batch_size}.json"

        # Format output with correct answers and accuracy
        formatted_output = format_output(all_comparisons, data_answers)

        with open(output_file, "w") as f:
            json.dump(formatted_output, f, indent=2)

        logging.info(f"Results saved to {output_file}")

def run_experiment(prompt_num, data_num, data_limit, batch_size):
    # get all data
    prompt = prompts[prompt_num]
    _data = data[data_num][:data_limit]
    _data_answers = data_answers[data_num][:data_limit]

    # batch data
    _data = get_batches(_data, batch_size)
    _data_answers = get_batches(_data_answers, batch_size)

    # run batched comparison with parallelization
    results = open_ai.compare_markets_batch(prompt, _data, concurrent_limit=40)
    save_results(prompt_num, data_num, data_limit, batch_size, _data_answers, results)

def format_markets_for_comparison(comparable_markets: list[list[dict]]) -> tuple[list[dict], list[dict]]:
    """
    Formats markets for LLM comparison.

    Returns:
        tuple of (comparisons, metadata):
        - comparisons: List of comparison objects for LLM
        - metadata: List of dicts with market IDs and canonical similarities
    """
    comparisons = []
    metadata = []
    comparison_counter = 1

    for event_group in comparable_markets:
        # Find the reference market (the source event)
        reference = None
        targets = []

        for market in event_group:
            if market['role'] == 'reference':
                reference = market
            else:
                targets.append(market)

        if not reference:
            logging.warning(f"No reference market found in group, skipping")
            continue

        # Create a comparison for reference vs each target
        for target in targets:
            # Parse outcomes if they're strings, otherwise use as-is
            ref_outcomes = reference['outcomes'] if isinstance(reference['outcomes'], list) else json.loads(reference['outcomes'])
            target_outcomes = target['outcomes'] if isinstance(target['outcomes'], list) else json.loads(target['outcomes'])

            comparison = {
                "comparison_id": f"comparison_{comparison_counter}",
                "market_1": {
                    "question": reference['question'],
                    "outcomes": ref_outcomes
                },
                "market_2": {
                    "question": target['question'],
                    "outcomes": target_outcomes
                }
            }
            comparisons.append(comparison)

            # Store metadata for this comparison
            metadata.append({
                "market_1_id": reference['id'],
                "market_2_id": target['id'],
                "market_1_canonical_similarity": reference.get('canonical_similarity', 1.0),
                "market_2_canonical_similarity": target.get('canonical_similarity', 0.0)
            })

            comparison_counter += 1

    return comparisons, metadata

async def compare_markets(event_ids):
    with Database() as db:
        comparable_markets = db.get_comporable_markets_batch(event_ids, limit=3)

    comparison_data, metadata = format_markets_for_comparison(comparable_markets)

    # Batch comparisons into groups of 3 (optimal batch size from performance testing)
    comparison_data_batched = get_batches(comparison_data, 3)

    prompt = prompts["9"]
    results = await open_ai.compare_markets_batch_async(prompt, comparison_data_batched, concurrent_limit=40)

    save_results(9, 0, 0, 0, [], results, metadata)


################################################################################################
####### MAIN ###################################################################################
################################################################################################

def basic_comparison_test(prompt_num, data_num, data_limit):
    logging.info(f"Using prompt {prompt_num}")
    logging.info(f"Using data {data_num}")
    prompt = prompts[prompt_num]
    _data = data[data_num][:data_limit]
    _data_answers = data_answers[data_num][:data_limit]
    results = open_ai.compare_markets(prompt, _data)
    save_results(prompt_num, data_num, data_limit, _data_answers, [results])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--promptnumber", type=str, help="the comparison prompt to send to chatgpt. found in /EXPERIMENTAL_SYSTEM_PROMTS/prompt_{--promptnumber}.py")
    parser.add_argument("--datanumber", type=str, help="the comparison data to send to chatgpt. found in /EXPERIMENTAL_TEST_DATA/data_{--datanumber}.py. Answers are found in /EXPERIMENTAL_TEST_DATA/data_answers_{--datanumber}.py")
    parser.add_argument("--datalimit", type=int, help="limit the number of comparison to this number", default=99999999)
    parser.add_argument("--batchsize", type=int, help="the number of comparisons we ask the llm to do in a single request", default=3)
    args = parser.parse_args()
    #run_experiment(args.promptnumber, args.datanumber, args.datalimit, args.batchsize)
    asyncio.run(compare_markets(['134117', '134115']))
    print("PROGRAM COMPLETE")