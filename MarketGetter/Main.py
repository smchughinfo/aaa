import requests
from pprint import pprint
import json

def get_markets(offset, limit=50):
    try:
        print(f'Getting markets at offset {offset}.')
        url = f'https://gamma-api.polymarket.com/events?order=id&ascending=false&closed=false&limit={limit}&offset={offset}'
        response = requests.get(url)
        events = response.json()
    except Exception as e:
        print(f"Error fetching markets: {e}")
        return None

    markets_full = []
    for event in events:
        for market in event["markets"]:
            market["event_id"] = event["id"]
        markets_full.extend(event["markets"])

    markets = []
    for m in markets_full:
        if m['closed'] or not m.get('bestBid') or not m.get('bestAsk') or not m.get('endDateIso'):
            continue
        
        markets.append({
            'event_id': m['event_id'],
            'question': m['question'],
            'bestBid': m.get('bestBid'),
            'bestAsk': m.get('bestAsk'),
            'outcomes': m['outcomes'],
            'endDate': m['endDateIso'],
            'id': m['id']    
        })
    
    return markets

markets = []
offset = 0
while True:
    page = get_markets(offset)
    if page is None or len(page) == 0: 
        break
    markets.extend(page)
    offset += 50

with open("markets.json", 'w') as f:
    json.dump(markets, f, indent=2)

print(f"Total markets collected: {len(markets)}")