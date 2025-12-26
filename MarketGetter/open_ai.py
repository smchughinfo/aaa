from openai import OpenAI
client = OpenAI()

model = "text-embedding-3-small"

def get_embedding(text):
    return client.embeddings.create(
        input=text,
        model=model
    ).data[0].embedding

if __name__ == "__main__":
    embedding = get_embedding("the cat in the hat")
    print(embedding)
