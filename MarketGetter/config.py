import os

host=os.environ["aaa_neon_db_host"]
database=os.environ["aaa_neon_db_database"]
user=os.environ["aaa_neon_db_username"]
password=os.environ["aaa_neon_db_password"]
connection_string = f"host={host} dbname={database} user={user} password={password} sslmode=require"

openai_api_key=os.environ["aaa_openai_api_key"]

canonical_question_prompt = """

The following questions and their corresponding outcomes are from a betting market. 
They are all part of a single event. 
Can you generate a canonical/aggregate/general version of these questions that represents the whole group.
For example the canonical version of the following questions:

['Will Yariv Levin be the next Prime Minister of Israel? (Yariv Levin)', 'Will Yair Lapid be the next Prime Minister of Israel? (Yair Lapid)', 'Will Yair Golan be the next Prime Minister of Israel? (Yair Golan)', 'Will Yoav Gallant be the next Prime Minister of Israel? (Yoav Gallant)', 'Will Yossi Cohen be the next Prime Minister of Israel? (Yossi Cohen)', 'Will Naftali Bennett be the next Prime Minister of Israel? (Naftali Bennett)', 'Will Israel Katz be the next Prime Minister of Israel? (Israel Katz)', 'Will Itamar Ben-Gvir be the next Prime Minister of Israel? (Itamar Ben-Gvir)', 'Will Gadi Eisenkot be the next Prime Minister of Israel? (Gadi Eisenkot)', 'Will Bezalel Smotrich be the next Prime Minister of Israel? (Bezalel Smotrich)', 'Will Benny Gantz be the next Prime Minister of Israel? (Benny Gantz)', 'Will Avigdor Lieberman be the next Prime Minister of Israel? (Avigdor Lieberman)']

Should be something like: "Who will be the prime minister of Israel"

Keep your canonical version of the question as similiar to the included questions as possible.
Included questions and their corresponding outcomes follow:

[DATA]"""