import argparse
import open_ai
import prettyprint
import json
from pathlib import Path
from EXPERIMENTAL_SYSTEM_PROMPTS import *
from EXPERIMENTAL_TEST_DATA import *

def save_results(prompt_num, data_num, data_limit, data_answers, results):
    output_dir = Path("EXPERIMENTAL_RESULTS")
    output_file = output_dir / f"{prompt_num}_{data_num}_{data_limit}.json"
    with open(output_file, "w") as f:
        f.write(results.to_json())

def run_experiment(prompt_num, data_num, data_limit):
    print("using prompt", prompt_num)
    print("using data", data_num)
    prompt = prompts[prompt_num][:data_limit]
    _data = data[data_num][:data_limit]
    _data_answers = data_answers[data_num][:data_limit]
    results = open_ai.compare_markets(prompt, _data)
    save_results(prompt_num, data_num, data_limit, _data_answers, results)

################################################################################################
####### MAIN ###################################################################################
################################################################################################

parser = argparse.ArgumentParser()
parser.add_argument("--promptnumber", type=str, help="the comparison prompt to send to chatgpt. found in /EXPERIMENTAL_SYSTEM_PROMTS/prompt_{--promptnumber}.py")
parser.add_argument("--datanumber", type=str, help="the comparison data to send to chatgpt. found in /EXPERIMENTAL_TEST_DATA/data_{--datanumber}.py. Answers are found in /EXPERIMENTAL_TEST_DATA/data_answers_{--datanumber}.py")
parser.add_argument("--datalimit", type=int, help="limit the number of comparison to this number", default=99999999)
args = parser.parse_args()
run_experiment(args.promptnumber, args.datanumber, args.datalimit)