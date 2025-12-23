import requests
from pprint import pprint
import json
from datetime import datetime

def _get_markets_from_kalshi_api(all_markets = [], cursor = None):
    cursor = "" if cursor is None else f"cursor={cursor}&"
    response = requests.get(f"https://api.elections.kalshi.com/trade-api/v2/events?{cursor}with_nested_markets=true&status=open&limit=200")
    events = response.json()

    events_count = len(events["events"])
    market_count = sum(len(x["markets"]) for x in events["events"])
    print(f"Retrieved {events_count} events with {market_count} markets using cursor {cursor}")

    cursor = events.get("cursor")

    for event in events["events"]:
        for market in event["markets"]:
            reduced_market = reduce_market(event, market)
            all_markets.extend(reduced_market)

    if cursor:
        _get_markets_from_kalshi_api(all_markets, cursor)

    return all_markets

def reduce_market(event, market):
    # we use polymarket field names for this object. reason = it seems like these should be normalized from the start and polymarket Getter was written first
    return {
        "event_id": event["event_ticker"],
        "question": market["title"],
        "bestBid": market["yes_bid"],
        "bestAsk": market["yes_ask"],
        "endDate": market["close_time"],
        "id": market["ticker"],
        "outcomes": ["Yes", "No"]
    }

def get_all_events():
    regular_event_markets = _get_markets_from_kalshi_api()
    with open("markets-kalshi-regular.json", "w") as f:
        json.dump(regular_event_markets, f, indent=2)
        pprint(f"Total events: {len(regular_event_markets)}")
    return regular_event_markets

if __name__ == "__main__":
    get_all_events()
