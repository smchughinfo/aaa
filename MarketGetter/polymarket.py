import requests
from pprint import pprint
import json
from database import Database

def _get_markets_from_polymarket_api(offset, limit=50):
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
            'endDate': m['endDateIso'],
            'id': m['id'],
            'outcomes': m['outcomes'],
            'platform': 'Polymarket'
        })
    
    return markets

def get_markets():
    markets = []
    offset = 0
    while True:
        page = _get_markets_from_polymarket_api(offset)
        if page is None or len(page) == 0: 
            break
        markets.extend(page)
        offset += 50

    with Database() as db:
        for i, market in enumerate(markets, start=1):
            if i % 100 == 0 or i == len(markets):
                print(f"{i}/{len(markets)}\tPolymarket Upserts {i/len(markets):.2%} complete.")
            db.upsert_market(market)

    #with open("markets-polymarket.json", 'w') as f:
        #json.dump(markets, f, indent=2)

    print(f"Total markets retrieved from API: {len(markets)}")

if __name__ == "__main__":
    get_markets()