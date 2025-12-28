import psycopg2
import config
import json
from datetime import datetime
import pprint
import re
import logging

class Database():
    def __enter__(self):
        logging.info("Entering: connecting to database")
        self.conn = psycopg2.connect(config.connection_string)
        return self  # This becomes the 'db' variable in the with
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        logging.info("Exiting: cleaning up")
        if exc_type is None:  # No exception occurred
            logging.info("  Success! Committing...")
            self.conn.commit()
        else:  # Exception occurred
            logging.info(f"  Error occurred: {exc_val}")
            logging.info("  Rolling back...")
            self.conn.rollback()
            
        self.conn.close()
        return False  # Don't suppress exceptions

    def get_uncompared_markets(self, limit=2):
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

    def sanitize_text_for_postgres(text: str) -> str:
        """Remove characters that break PostgreSQL text fields"""
        if not text:
            return text
        
        # Remove null bytes
        text = text.replace('\x00', '')
        
        # Optionally remove other control characters (except newlines/tabs)
        # This removes characters like \x01, \x02, etc. but keeps \n and \t
        text = re.sub(r'[\x00-\x08\x0B-\x0C\x0E-\x1F\x7F]', '', text)
        
        return text

################################################################################################
####### MAIN ###################################################################################
################################################################################################

def test_select():
    with Database() as db:
        markets = db.get_unprocessed_events()
        logging.info(markets)
        logging.info(123)

if __name__ == "__main__":
    test_select()