import requests
from pprint import pprint

response = requests.get('https://gamma-api.polymarket.com/events?order=id&ascending=false&closed=false&limit=50&offset=5300')
data = response.json()

markets_full = []
for d in data:
    markets_full.extend(d["markets"])

markets = []
for m in markets_full:
    if m['closed'] or not m.get('bestBid') or not m.get('bestAsk') or not m.get('endDateIso'):
        continue
    
    markets.append({
        'question': m['question'],
        'bestBid': m.get('bestBid'),
        'bestAsk': m.get('bestAsk'),
        'outcomes': m['outcomes'],
        'endDate': m['endDateIso'],
        'id': m['id']    
    })

pprint(markets)