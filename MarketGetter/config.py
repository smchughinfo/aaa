import os

host=os.environ["aaa_neon_db_host"]
database=os.environ["aaa_neon_db_database"]
user=os.environ["aaa_neon_db_username"]
password=os.environ["aaa_neon_db_password"]
connection_string = f"host={host} dbname={database} user={user} password={password} sslmode=require"

openai_api_key=os.environ["aaa_openai_api_key"]

canonical_question_prompt = "The following questions and their corresponding outcomes are from a betting market. They are all part of a single event. Can you generate a canonical/generalized version of these questions that we can assign to that event for the purpose of generating embeddings. Keep your canonical version of the question as similiar to the included questions as possible. Included questions and their corresponding outcomes follow:\r\r[DATA]"