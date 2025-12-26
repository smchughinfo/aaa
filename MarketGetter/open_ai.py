from openai import OpenAI
import config

client = OpenAI(api_key=config.openai_api_key)

model = "text-embedding-3-small"

def get_embedding(text):
    return client.embeddings.create(
        input=text,
        model=model
    ).data[0].embedding

def get_embeddings_batch(texts):
    """Batch embeddings - pass a list"""
    response = client.embeddings.create(
        input=texts,
        model=model
    )
    return [item.embedding for item in response.data]

if __name__ == "__main__":
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

