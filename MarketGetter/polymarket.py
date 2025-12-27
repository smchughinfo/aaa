import requests
from pprint import pprint
import json
from database import Database

def _get_markets_page_from_polymarket_api(offset, limit=50):
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

    markets = {}
    for m in markets_full:
        if m['closed'] or not m.get('bestBid') or not m.get('bestAsk') or not m.get('endDateIso'):
            continue

        markets[m['id']] = {
            'event_id': m['event_id'],
            'question': m['question'],
            'bestBid': m.get('bestBid'),
            'bestAsk': m.get('bestAsk'),
            'endDate': m['endDateIso'],
            'id': m['id'],
            'outcomes': m['outcomes'],
            'platform': 'Polymarket'
        }

    return markets

def _get_markets_from_polymarket_api():
    markets = {}
    offset = 0
    while True:
        page = _get_markets_page_from_polymarket_api(offset)
        if not page: 
            break
        markets = markets | page
        offset += 50
    return markets

def save_markets():
    markets = _get_markets_from_polymarket_api()    
    with open("markets-polymarket.json", 'w') as f:
        json.dump(list(markets.values()), f, indent=2)

    if len(markets) == 0:
        print(f"0 Markers returned! Were we rate limited?")
        return

    print(f"Total markets retrieved from API: {len(markets)}")

    with Database() as db:
        unique_event_ids = {market['event_id'] for market in markets.values()}
        unique_event_ids = list(unique_event_ids)
        db.upsert_events_bulk(unique_event_ids)

    with Database() as db:
        print(f"Upserting {len(markets)} markets in bulk...")
        db.upsert_markets_bulk(markets.values())
        print(f"Bulk upsert complete!")

################################################################################################
####### MAIN ###################################################################################
################################################################################################

if __name__ == "__main__":
    save_markets()