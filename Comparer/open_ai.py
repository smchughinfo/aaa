from typing import List, Literal
from pydantic import BaseModel
import ast, json, pprint
import asyncio
from openai import OpenAI, AsyncOpenAI
import config

################################################################################################
####### VARIABLES ##############################################################################
################################################################################################

client = OpenAI(api_key=config.openai_api_key)
async_client = AsyncOpenAI(api_key=config.openai_api_key)

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
    """Synchronous version - compares a single batch of markets"""
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

async def compare_markets_async(prompt, test_data):
    """Async version - compares a single batch of markets"""
    user_json = json.dumps(test_data, indent=2)

    resp = await async_client.responses.parse(
        model=model,
        input=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_json},
        ],
        text_format=MarketComparisonList,
    )

    return resp.output_parsed

async def compare_markets_batch_async(prompt, test_data_list, concurrent_limit=20):
    """
    Process multiple batches of market comparisons in parallel.

    Args:
        prompt: The system prompt for comparisons
        test_data_list: List of test data batches (each batch is a list of market pairs)
        concurrent_limit: Max number of concurrent API calls

    Returns:
        List of MarketComparisonList objects
    """
    async def process_batch(idx, batch_data):
        result = await compare_markets_async(prompt, batch_data)
        print(f"Processed batch {idx+1}/{len(test_data_list)}")
        return result

    results = [None] * len(test_data_list)

    # Process in chunks to avoid overwhelming the API
    for chunk_start in range(0, len(test_data_list), concurrent_limit):
        chunk_end = min(chunk_start + concurrent_limit, len(test_data_list))
        chunk_tasks = [
            process_batch(i, test_data_list[i])
            for i in range(chunk_start, chunk_end)
        ]
        chunk_results = await asyncio.gather(*chunk_tasks)
        for i, result in enumerate(chunk_results):
            results[chunk_start + i] = result

    return results

def compare_markets_batch(prompt, test_data_list, concurrent_limit=20):
    """Synchronous wrapper for batch processing"""
    return asyncio.run(compare_markets_batch_async(prompt, test_data_list, concurrent_limit))

################################################################################################
####### MAIN ###################################################################################
################################################################################################

def test_compare_markets():
    compare_markets()

if __name__ == "__main__":
   test_compare_markets()

