import argparse
import open_ai
import prettyprint
import json
from pathlib import Path
from EXPERIMENTAL_SYSTEM_PROMPTS import *
from EXPERIMENTAL_TEST_DATA import *

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
    """
    Format results by adding correct answers and accuracy check.

    Args:
        comparisons: List of MarketComparison objects
        data_answers_batched: Batched list of correct answers (list of lists)

    Returns:
        List of dicts with comparison data + correct_answer + categorized_correctly
    """
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

def save_results(prompt_num, data_num, data_limit, batch_size, data_answers, results):
    output_dir = Path("EXPERIMENTAL_RESULTS")
    output_dir.mkdir(exist_ok=True)  # Create dir if doesn't exist
    output_file = output_dir / f"{prompt_num}_{data_num}_{data_limit}_{batch_size}.json"

    # Combine all batch results into one list
    all_comparisons = []
    for batch_result in results:
        all_comparisons.extend(batch_result.comparisons)

    # Format output with correct answers and accuracy
    formatted_output = format_output(all_comparisons, data_answers)

    with open(output_file, "w") as f:
        json.dump(formatted_output, f, indent=2)

def run_experiment(prompt_num, data_num, data_limit, batch_size):
    # get all data
    prompt = prompts[prompt_num]
    _data = data[data_num][:data_limit]
    _data_answers = data_answers[data_num][:data_limit]

    # batch data
    _data = get_batches(_data, batch_size)
    _data_answers = get_batches(_data_answers, batch_size)

    # run batched comparison with parallelization
    results = open_ai.compare_markets_batch(prompt, _data, concurrent_limit=20)
    save_results(prompt_num, data_num, data_limit, batch_size, _data_answers, results)

################################################################################################
####### MAIN ###################################################################################
################################################################################################

def basic_comparison_test(prompt_num, data_num, data_limit):
    print("using prompt", prompt_num)
    print("using data", data_num)
    prompt = prompts[prompt_num]
    _data = data[data_num][:data_limit]
    _data_answers = data_answers[data_num][:data_limit]
    results = open_ai.compare_markets(prompt, _data)
    save_results(prompt_num, data_num, data_limit, _data_answers, [results])

parser = argparse.ArgumentParser()
parser.add_argument("--promptnumber", type=str, help="the comparison prompt to send to chatgpt. found in /EXPERIMENTAL_SYSTEM_PROMTS/prompt_{--promptnumber}.py")
parser.add_argument("--datanumber", type=str, help="the comparison data to send to chatgpt. found in /EXPERIMENTAL_TEST_DATA/data_{--datanumber}.py. Answers are found in /EXPERIMENTAL_TEST_DATA/data_answers_{--datanumber}.py")
parser.add_argument("--datalimit", type=int, help="limit the number of comparison to this number", default=99999999)
parser.add_argument("--batchsize", type=int, help="the number of comparisons we ask the llm to do in a single request", default=10)
args = parser.parse_args()
run_experiment(args.promptnumber, args.datanumber, args.datalimit, args.batchsize)