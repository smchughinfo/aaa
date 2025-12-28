import requests
from pprint import pprint
import json
from datetime import datetime
from database import Database
import logging
import config

def _get_markets_from_kalshi_api(all_markets = None, cursor = None):
    if all_markets is None:
        all_markets = {}

    cursor = "" if cursor is None else f"cursor={cursor}&"
    response = requests.get(f"https://api.elections.kalshi.com/trade-api/v2/events?{cursor}with_nested_markets=true&status=open&limit=200")
    events = response.json()

    events_count = len(events["events"])
    market_count = sum(len(x["markets"]) for x in events["events"])
    logging.info(f"Retrieved {events_count} events with {market_count} markets using cursor '{cursor}'")

    cursor = events.get("cursor")

    for event in events["events"]:
        for market in event["markets"]:
            reduced_market = reduce_market(event, market)
            all_markets[reduced_market['id']] = reduced_market

    if cursor:
        _get_markets_from_kalshi_api(all_markets, cursor)

    return all_markets

def reduce_market(event, market):
    # we use polymarket field names for this object. reason = it seems like these should be normalized from the start and polymarket Getter was written first
    question = market["title"]
    question = f"{question} ({market['yes_sub_title']})"

    return {
        "event_id": event["event_ticker"],
        "question": question,
        "bestBid": market["yes_bid"],
        "bestAsk": market["yes_ask"],
        "endDate": market["close_time"],
        "id": market["ticker"],
        "outcomes": ["Yes", "No"],
        'platform': 'Kalshi'
    }

def save_markets():
    markets = _get_markets_from_kalshi_api()

    if config.on_dev:
        with open("markets-kalshi.json", "w") as f:
            json.dump(list(markets.values()), f, indent=2)

    logging.info(f"Total markets retrieved from API: {len(markets)}")

    with Database() as db:
        unique_event_ids = {market['event_id'] for market in markets.values()}
        unique_event_ids = list(unique_event_ids)
        db.upsert_events_bulk(unique_event_ids)

    with Database() as db:
        logging.info(f"Upserting {len(markets)} markets in bulk...")
        db.upsert_markets_bulk(list(markets.values()))
        logging.info(f"Bulk upsert complete!")

################################################################################################
####### MAIN ###################################################################################
################################################################################################

if __name__ == "__main__":
    save_markets()
