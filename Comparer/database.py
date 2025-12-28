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

    def get_comporable_markets(self, event_id, limit=5) -> list:
        '''
        Includes self. e.g. Includes the markets for the provided event_id
        
        :param event_id: The event_id of the event whose question will be used to find similiar events.
        :param limit: The n events whose question is most similiar to event_id's question.
        :return: All markets for similiar events
        :rtype: list
        '''
        limit = limit + 1 # add 1 because we include markets for the supplied event_id so we to get 1 additional event to get {limit} matches
        cursor = self.conn.cursor()
        sql =   f"""
                    WITH source AS (
                        SELECT embedding 
                        FROM events 
                        WHERE id = %s 
                        LIMIT 1
                    ),
                    similiar_events AS (
                    SELECT 
                        ID
                        FROM events e
                        CROSS JOIN source s
                        WHERE e.embedding IS NOT NULL
                        ORDER BY e.embedding <=> s.embedding
                        LIMIT %s
                    )
                    SELECT id, event_id, question, outcomes
                    FROM Markets m
                    WHERE m.event_id in (
                        SELECT id
                        FROM similiar_events
                    )
                """
        cursor.execute(sql, (event_id, limit))
        markets = []
        for row in cursor:
            markets.append({
                "id": row[0],
                "role": "reference" if row[0] == event_id else "target",
                "event_id": row[1],
                "question": row[2],
                "outcomes": row[3],
            })

        return markets

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
        markets = db.get_comporable_markets("KXELONMARS-99")
        logging.info(markets)
        logging.info(123)

if __name__ == "__main__":
    test_select()