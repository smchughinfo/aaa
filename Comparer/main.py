import argparse
from EXPERIMENTAL_SYSTEM_PROMPTS import *
import open_ai

def run_experiment(prompt_num, data_num):
    print("using prompt", prompt_num)
    print("using data", data_num)
    prompt = prompts[prompt_num]
    data = prompts[data_num]
    open_ai.compare_markets(prompt, data)

################################################################################################
####### MAIN ###################################################################################
################################################################################################

parser = argparse.ArgumentParser()
parser.add_argument("--promptnumber", type=str)
parser.add_argument("--datanumber", type=str)
args = parser.parse_args()
run_experiment(args.promptnumber, args.datanumber)