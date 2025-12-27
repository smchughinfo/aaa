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

    def upsert_markets_bulk(self, markets):
        cursor = self.conn.cursor()

        # Build values list
        values = []
        now = datetime.utcnow()
        for m in markets:
            values.extend([
                m['id'],
                m['event_id'],
                m['question'],
                m['bestBid'],
                m['bestAsk'],
                m['endDate'],
                json.dumps(m['outcomes']),
                m['platform'],
                now
            ])

        # Create placeholders: (%s, %s, ...), (%s, %s, ...), ...
        placeholders = ','.join(['(%s,%s,%s,%s,%s,%s,%s,%s,%s)'] * len(markets))

        query = f"""
            INSERT INTO markets (id, event_id, question, best_bid, best_ask, end_date, outcomes, platform, last_updated)
            VALUES {placeholders}
            ON CONFLICT (id) DO UPDATE SET
                best_bid = EXCLUDED.best_bid,
                best_ask = EXCLUDED.best_ask,
                last_updated = EXCLUDED.last_updated
        """

        cursor.execute(query, values)

    def upsert_events_bulk(self, events):
        cursor = self.conn.cursor()

        placeholders = ','.join(['(%s)'] * len(events))

        query = f"""
            INSERT INTO events (id)
            VALUES {placeholders}
            ON CONFLICT (id) DO NOTHING
        """

        cursor.execute(query, events)

    def get_events_that_need_embeddings(self, limit=1000):
        cursor = self.conn.cursor()
        sql =   f"""
                    SELECT e.id, m.question, m.outcomes
                    FROM markets m 
                    JOIN events e
                    ON m.event_id = e.id
                    WHERE e.question IS NULL
                    LIMIT %s;
                """
        cursor.execute(sql, (limit,))
        markets = []
        for row in cursor:
            markets.append(row)

        events = {}

        if len(markets) > 0:
            last_event_id = markets[-1][0] # throw this one away. because of the limit we may not have selected all markets for the last event
            for market in markets:
                event = events.get(market[0], { "questions": [], "outcomes": [] })
                event["questions"].append(market[1])
                event["outcomes"].append(market[2])
                events[market[0]] = event
            del events[last_event_id]

        return events

################################################################################################
####### MAIN ###################################################################################
################################################################################################

def test_upsert():
    markets = None
    #with open("markets-polymarket.json") as f:
    with open("markets-kalshi.json") as f:
        markets = json.load(f)

    with Database() as db:
        for market in markets:
            db.upsert_market(market)
            print("UPSERT SUCCESS")
            break

def test_select():
    with Database() as db:
        markets = db.get_events_that_need_embeddings()
        print(markets)
        print(123)

if __name__ == "__main__":
    test_select()