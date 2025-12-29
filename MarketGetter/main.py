import polymarket
import kalshi
import time
import event_processor
import argparse
import service_bus
import logging

def batch_event_id_list(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]


################################################################################################
####### MAIN ###################################################################################
################################################################################################

def run_once():
    polymarket.save_markets()
    kalshi.save_markets()
    processed_event_ids = event_processor.process_new_events()
    batched_event_ids = batch_event_id_list(processed_event_ids, 100)
    for event_ids in batched_event_ids:
        service_bus.queue_message(event_ids)
    # todo: add a compared column to markets. comparer function sets this to true. 
    # ....then right here you check the db for all non-compared markets (have been missed for some reason, potentially error)
    
def loop():
    i = 1
    wait_time = 15 # minutes
    while True:
        run_once()
        logging.info(f"saved markets {i} times. going into {wait_time} minutes sleep")
        i += 1
        for j in range(0, wait_time):
            time.sleep(60*1)
            logging.info(f"{wait_time-(j+1)} minutes remaining before next poll")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--loop", action="store_true", help="Run continuously")
    parms = parser.parse_args()

    if parms.loop:
        loop()
    else:
        run_once()













################################################################################################
#### OLD JUNK ##################################################################################
################################################################################################


################ CHECK MARKETS-*.JSON FILES FOR DUPLICATE MARKET IDS
############ import json
############ from pprint import pprint
############ 
############ def group_markets_by_id(file):
############     grouped_list = {}
############     with open(file, "r") as f:
############         raw_markets = json.load(f)
############         
############         for market in raw_markets:
############             dup_markets = grouped_list.get(market["id"], [])
############             dup_markets.append(market)
############             grouped_list[market["id"]] = dup_markets
############ 
############     return grouped_list
############ 
############ def get_duplicate_markets(grouped_list):
############     reduced = []
############     for markets in grouped_list.values():
############         if len(markets) > 1:
############             reduced.append(markets)
############     return reduced
############ 
############ def list_dups(file):
############     market_counts = group_markets_by_id(file)
############     dup_markets = get_duplicate_markets(market_counts)
############     plogging.info(dup_markets)
############ 
############ logging.info("Polymarket Duplicates")
############ list_dups("markets-polymarket.json")
############ logging.info("Kalshi Duplicates")
############ list_dups("markets-kalshi.json")
############ 
############ logging.info(123)