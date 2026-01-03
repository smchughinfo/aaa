from database import Database
import open_ai
import asyncio
import logging

async def process_next_new_event_batch_async():
    processed_events = []
    with Database() as db:
        unprocessed_events = db.get_unprocessed_events()

    if unprocessed_events:
        canonical_questions = await open_ai.get_canonical_questions_async(unprocessed_events)
        embeddings = open_ai.get_embeddings_batch(canonical_questions)

        for i, k in enumerate(unprocessed_events):
            processed_events.append({
                'id': k,
                'question': canonical_questions[i],
                'embedding': embeddings[i],
            })
    return processed_events

async def process_new_events_async():
    event_ids = []
    batch_num = 1
    while True:
        batch = await process_next_new_event_batch_async()
        if not batch:
            break
        logging.info(f"Processing batch {batch_num}")
        with Database() as db:
            db.upsert_events_bulk(batch)
            batch_event_ids = [x["id"] for x in batch]
            event_ids.extend(batch_event_ids)
        batch_num += 1
    return event_ids

def process_new_events():
    """Synchronous wrapper for async event processing"""
    return asyncio.run(process_new_events_async())

################################################################################################
####### MAIN ###################################################################################
################################################################################################

if __name__ == "__main__":
   process_new_events()