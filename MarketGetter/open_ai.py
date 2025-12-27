from openai import OpenAI
import config
import json
from database import Database

client = OpenAI(api_key=config.openai_api_key)

embedding_model = "text-embedding-3-small"
canonicalization_model = "gpt-4o-mini"

def get_embedding(text):
    return client.embeddings.create(
        input=text,
        model=embedding_model
    ).data[0].embedding

from openai import OpenAI
import json
import config
from pydantic import BaseModel

client = OpenAI(api_key=config.openai_api_key)

class CanonicalOut(BaseModel):
    canonical_question: str

def get_canonical_question(prompt: str) -> str:
    resp = client.responses.parse(
        model=canonicalization_model,
        input=[
            {"role": "system", "content": "You normalize prediction market questions to canonical form."},
            {"role": "user", "content": prompt},
        ],
        text_format=CanonicalOut,
    )
    return resp.output_parsed.canonical_question

def get_canonical_questions(markets):
    canonical_questions = []
    for i, market in enumerate(markets.values()):
        canonical_question = None
        if len(market["questions"]) == 1:
            canonical_question = market["questions"][0]
        else:
            data = json.dumps(market)
            prompt = config.canonical_question_prompt.replace("[DATA]", data)
            canonical_question = get_canonical_question(prompt)
        canonical_questions.append(canonical_question)
        print(f"Generate Canonical - {i+1}/{len(markets)} - {canonical_question}")
    return canonical_questions

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

def openai_embeddings_test():
     # Single
    single = get_embedding("the cat in the hat")
    print(f"Single embedding (first 5): {single[:5]}")
    
    # Batch
    texts = [
        "the cat in the hat",
        "green eggs and ham", 
        "one fish two fish"
    ]
    embeddings = get_embeddings_batch(texts)
    
    print(f"\nBatch size: {len(embeddings)}")
    for i, emb in enumerate(embeddings):
        print(f"Embedding {i} (first 5): {emb[:5]}")

def process_next_new_event_batch():    
    processed_events = []
    with Database() as db:
        unprocessed_events = db.get_unprocessed_events()
    
    if unprocessed_events:
        unprocessed_events =  dict(list(unprocessed_events.items())[:3])
        canonical_questions = get_canonical_questions(unprocessed_events)
        embeddings = get_embeddings_batch(canonical_questions)
        
        for i, k in enumerate(unprocessed_events):
            processed_events.append({
                'id': k,
                'question': canonical_questions[i],
                'embedding': embeddings[i],
            })
    return processed_events

def process_new_events():
    batch_num = 1
    while batch := process_next_new_event_batch():
        print(f"Processing batch {batch_num}")
        with Database() as db:
            db.upsert_events_bulk(batch)
        batch_num += 1

if __name__ == "__main__":
   process_new_events()

