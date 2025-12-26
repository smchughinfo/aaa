import polymarket
import kalshi
import time

i = 1
while True:
    polymarket.save_markets()
    kalshi.save_markets()
    print(f"saved markets {i} times. going into 15 minutes sleep")
    i += 1
    for j in range(0, 15):
        time.sleep(60*1)
        print(f"{15-(j+1)} minutes remaining before next poll")

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
############     pprint(dup_markets)
############ 
############ print("Polymarket Duplicates")
############ list_dups("markets-polymarket.json")
############ print("Kalshi Duplicates")
############ list_dups("markets-kalshi.json")
############ 
############ print(123)