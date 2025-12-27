from database import Database
import open_ai

def process_next_new_event_batch():    
    processed_events = []
    with Database() as db:
        unprocessed_events = db.get_unprocessed_events()
    
    if unprocessed_events:
        #unprocessed_events =  dict(list(unprocessed_events.items())[:3])
        canonical_questions = open_ai.get_canonical_questions(unprocessed_events)
        embeddings = open_ai.get_embeddings_batch(canonical_questions)
        
        for i, k in enumerate(unprocessed_events):
            processed_events.append({
                'id': k,
                'question': canonical_questions[i],
                'embedding': embeddings[i],
            })
    return processed_events

def process_new_events():
    event_ids = []
    batch_num = 1
    while batch := process_next_new_event_batch():
        print(f"Processing batch {batch_num}")
        with Database() as db:
            db.upsert_events_bulk(batch)
            batch_event_ids = [x["id"] for x in batch]
            event_ids.extend(batch_event_ids)
        batch_num += 1
    return event_ids

################################################################################################
####### MAIN ###################################################################################
################################################################################################

if __name__ == "__main__":
   process_new_events()