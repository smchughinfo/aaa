from openai import OpenAI, AsyncOpenAI
import config
import json
import asyncio
from database import Database
from pydantic import BaseModel
import logging

client = OpenAI(api_key=config.openai_api_key)
async_client = AsyncOpenAI(api_key=config.openai_api_key)

embedding_model = "text-embedding-3-small"
canonicalization_model = "gpt-4o-mini"

def get_embedding(text):
    return client.embeddings.create(
        input=text,
        model=embedding_model
    ).data[0].embedding

class CanonicalOut(BaseModel):
    canonical_question: str

async def get_canonical_question_async(prompt: str) -> str:
    resp = await async_client.responses.parse(
        model=canonicalization_model,
        input=[
            {"role": "system", "content": "You normalize prediction market questions to canonical form."},
            {"role": "user", "content": prompt},
        ],
        text_format=CanonicalOut,
    )
    canonical_response = resp.output_parsed.canonical_question
    canonical_response = Database.sanitize_text_for_postgres(canonical_response)
    return canonical_response

async def get_canonical_questions_async(markets, concurrent_limit=20):
    async def process_market(idx, market):
        if len(market["questions"]) == 1:
            canonical_q = market["questions"][0]
        else:
            data = json.dumps(market)
            prompt = config.canonical_question_prompt.replace("[DATA]", data)
            canonical_q = await get_canonical_question_async(prompt)
        logging.info(f"Generate Canonical - {idx+1}/{len(markets)} - {canonical_q}")
        return canonical_q

    markets_list = list(markets.values())
    results = [None] * len(markets_list)

    # Process in chunks to avoid overwhelming the API
    for chunk_start in range(0, len(markets_list), concurrent_limit):
        chunk_end = min(chunk_start + concurrent_limit, len(markets_list))
        chunk_tasks = [
            process_market(i, markets_list[i])
            for i in range(chunk_start, chunk_end)
        ]
        chunk_results = await asyncio.gather(*chunk_tasks)
        for i, result in enumerate(chunk_results):
            results[chunk_start + i] = result

    return results

def get_canonical_questions(markets):
    return asyncio.run(get_canonical_questions_async(markets))

async def process_next_new_event_batch_async():
    processed_events = []
    with Database() as db:
        unprocessed_events = db.get_unprocessed_events()

    if unprocessed_events:
        unprocessed_events = dict(list(unprocessed_events.items())[:3])
        canonical_questions = await get_canonical_questions_async(unprocessed_events)
        embeddings = get_embeddings_batch(canonical_questions)

        for i, k in enumerate(unprocessed_events):
            processed_events.append({
                'id': k,
                'question': canonical_questions[i],
                'embedding': embeddings[i],
            })
    return processed_events

async def process_new_events_async():
    batch_num = 1
    while True:
        batch = await process_next_new_event_batch_async()
        if not batch:
            break
        logging.info(f"Processing batch {batch_num}")
        with Database() as db:
            db.upsert_events_bulk(batch)
        batch_num += 1

def get_embeddings_batch(texts):
    if len(texts) > 1000:
        raise ValueError("Embedding batch size is limited to 1000")
    response = client.embeddings.create(
        input=texts,
        model=embedding_model
    )
    return [item.embedding for item in response.data]

################################################################################################
####### MAIN ###################################################################################
################################################################################################

def process_new_events():
    """Synchronous wrapper for async event processing"""
    asyncio.run(process_new_events_async())

def openai_embeddings_test():
     # Single
    single = get_embedding("the cat in the hat")
    logging.info(f"Single embedding (first 5): {single[:5]}")
    
    # Batch
    texts = [
        "the cat in the hat",
        "green eggs and ham", 
        "one fish two fish"
    ]
    embeddings = get_embeddings_batch(texts)
    
    logging.info(f"\nBatch size: {len(embeddings)}")
    for i, emb in enumerate(embeddings):
        logging.info(f"Embedding {i} (first 5): {emb[:5]}")

if __name__ == "__main__":
   openai_embeddings_test()

