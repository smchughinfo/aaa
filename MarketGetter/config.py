import os

host=os.environ["aaa_neon_db_host"]
database=os.environ["aaa_neon_db_database"]
user=os.environ["aaa_neon_db_username"]
password=os.environ["aaa_neon_db_password"]
connection_string = f"host={host} dbname={database} user={user} password={password} sslmode=require"

openai_api_key=os.environ["aaa_openai_api_key"]