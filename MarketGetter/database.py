import psycopg2
import config
import json
from datetime import datetime
import pprint

class Database():
    def __enter__(self):
        print("Entering: connecting to database")
        self.conn = psycopg2.connect(config.connection_string)
        return self  # This becomes the 'db' variable in the with
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting: cleaning up")
        if exc_type is None:  # No exception occurred
            print("  Success! Committing...")
            self.conn.commit()
        else:  # Exception occurred
            print(f"  Error occurred: {exc_val}")
            print("  Rolling back...")
            self.conn.rollback()
            
        self.conn.close()
        return False  # Don't suppress exceptions

    def upsert_market(self, market):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO markets (id, event_id, question, best_bid, best_ask, end_date, outcomes, platform, last_updated)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (id) DO UPDATE SET
                best_bid = EXCLUDED.best_bid,
                best_ask = EXCLUDED.best_ask,
                last_updated = EXCLUDED.last_updated
        """, (
            market['id'],
            market['event_id'],
            market['question'],
            market['bestBid'],
            market['bestAsk'],
            market['endDate'],
            json.dumps(market['outcomes']),  # Convert list to JSON string
            'Polymarket',
            datetime.utcnow()
        ))
        self.conn.commit()
        cursor.close()

if __name__ == "__main__":
    database = Database()

    markets = None
    #with open("markets-polymarket.json") as f:
    with open("markets-kalshi.json") as f:
        markets = json.load(f)

    with Database() as db:
        for market in markets:
            db.upsert_market(market)
            print("UPSERT SUCCESS")
            break
        
