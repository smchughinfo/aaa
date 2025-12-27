from openai import OpenAI
import config
import json

client = OpenAI(api_key=config.openai_api_key)

embedding_model = "text-embedding-3-small"
canonicalization_model = "chatgpt-4o-latest"

def get_embedding(text):
    return client.embeddings.create(
        input=text,
        model=embedding_model
    ).data[0].embedding

def get_canonical_question(prompt):
    completion = client.chat.completions.create(
        model=canonicalization_model,
        messages=[
            {"role": "developer", "content": "You normalize prediction market questions to canonical form."},
            {"role": "user", "content": prompt}
        ]
    )
    return completion

def get_canonical_questions(markets):
    for market in markets.values():
        data = json.dumps(market)
        prompt = config.canonical_question_prompt.replace("[DATA]", data)
        get_canonical_question(prompt)

def get_embeddings_batch(texts):
    """Batch embeddings - pass a list"""
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

def get_canonical_question_test():
    from database import Database
    with Database() as db:
        markets = db.get_events_that_need_embeddings()
        get_canonical_questions(markets)
        print(markets)
    pass

if __name__ == "__main__":
   get_canonical_question_test()

