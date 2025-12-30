from typing import List, Literal
from pydantic import BaseModel
import ast, json, pprint
from openai import OpenAI
import config

################################################################################################
####### VARIABLES ##############################################################################
################################################################################################

client = OpenAI(api_key=config.openai_api_key)

model = "gpt-4o-mini"

################################################################################################
####### HELPER CLASSES #########################################################################
################################################################################################

from typing import Literal, Optional

class MarketComparison(BaseModel):
    market_id1: str
    market_id2: str
    relationship: Literal["EQUIVALENT","NEGATION","SUBSET","SUPERSET","OVERLAP","UNRELATED","UNCERTAIN"]
    arbitrage_match: bool
    notes: str

class MarketComparisonList(BaseModel):
    comparisons: List[MarketComparison]

    def to_json(self):
        return self.model_dump_json(indent=2)
    
################################################################################################
####### LOGIC ##################################################################################
################################################################################################

def compare_markets(prompt, test_data):
    user_json = json.dumps(test_data, indent=2)

    resp = client.responses.parse(
        model=model,
        input=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_json},
        ],
        text_format=MarketComparisonList,
    )

    return resp.output_parsed

################################################################################################
####### MAIN ###################################################################################
################################################################################################

def test_compare_markets():
    compare_markets()

if __name__ == "__main__":
   test_compare_markets()

