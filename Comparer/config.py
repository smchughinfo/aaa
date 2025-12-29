import os

# Check if running on local dev machine vs Azure
on_dev = os.environ.get("aaa_on_dev", "false").lower() == "true"

host=os.environ["aaa_neon_db_host"]
database=os.environ["aaa_neon_db_database"]
user=os.environ["aaa_neon_db_username"]
password=os.environ["aaa_neon_db_password"]
connection_string = f"host={host} dbname={database} user={user} password={password} sslmode=require"

openai_api_key=os.environ["aaa_comparer_openai_api_key"]
aaa_sb_aaa_connection_string= os.environ["aaa_sb_aaa_connection_string"]


