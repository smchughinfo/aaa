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

    def get_comporable_markets_batch(self, event_ids: list[str], limit=5, batch_size = 10) -> list[list]:
        '''
        Get comparable markets for multiple events at once.

        :param event_ids: List of event_ids to find comparable markets for
        :param limit: The n events whose question is most similar to each event_id's question
        :return: List of lists - one list of markets per event_id, in same order as input
        :rtype: list[list]
        '''
        if not event_ids:
            return []

        cursor = self.conn.cursor()
        results = []

        # Process in batches of 10 to avoid overwhelming the DB
        for i in range(0, len(event_ids), batch_size):
            batch = event_ids[i:i + batch_size]

            for event_id in batch:
                markets = self._get_markets_for_event(cursor, event_id, limit)
                results.append(markets)

        return results

    def _get_markets_for_event(self, cursor, event_id: str, limit: int) -> list:
        '''
        Helper method to get markets for a single event (reused logic from get_comporable_markets)
        '''
        actual_limit = limit + 1  # +1 because we include the source event

        sql = """
            WITH source AS (
                SELECT embedding
                FROM events
                WHERE id = %s
                LIMIT 1
            ),
            similar_events AS (
                SELECT
                    e.ID,
                    1 - (e.embedding <=> s.embedding) as similarity
                FROM events e
                CROSS JOIN source s
                WHERE e.embedding IS NOT NULL
                ORDER BY e.embedding <=> s.embedding
                LIMIT %s
            )
            SELECT m.id, m.event_id, m.question, m.outcomes, se.similarity
            FROM Markets m
            JOIN similar_events se ON m.event_id = se.ID
        """

        cursor.execute(sql, (event_id, actual_limit))
        markets = []
        for row in cursor:
            markets.append({
                "id": row[0],
                "role": "reference" if row[1] == event_id else "target",
                "event_id": row[1],
                "question": row[2],
                "outcomes": row[3],
                "canonical_similarity": row[4],
            })

        return markets

    def get_comporable_markets(self, event_id, limit=5) -> list:
        '''
        Includes self. e.g. Includes the markets for the provided event_id

        :param event_id: The event_id of the event whose question will be used to find similiar events.
        :param limit: The n events whose question is most similiar to event_id's question.
        :return: All markets for similiar events
        :rtype: list
        '''
        cursor = self.conn.cursor()
        return self._get_markets_for_event(cursor, event_id, limit)

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

    def upsert_comparison(self, comparison):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO comparisons (market_1_id, market_2_id, comparable, canonical_similarity)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (market_1_id, market_2_id) DO UPDATE SET
                comparable = EXCLUDED.comparable,
                canonical_similarity = EXCLUDED.canonical_similarity
        """, (
            comparison['market_1_id'],
            comparison['market_2_id'],
            comparison['comparable'],
            comparison['canonical_similarity']
        ))
        self.conn.commit()
        cursor.close()

################################################################################################
####### MAIN ###################################################################################
################################################################################################

def test_select():
    with Database() as db:

        db.upsert_comparison(comparison = {
            'market_1_id': '1078262',
            'market_2_id': '1078263',
            'comparable': True,
            'canonical_similarity': 0.87
        })

        #markets = db.get_comporable_markets("KXELONMARS-99")
        #logging.info(markets)
        logging.info(123)

def test_batch_select():
    with Database() as db:
        event_ids = ["KXELONMARS-99", "KXELONMARS-100", "KXELONMARS-101"]
        batch_results = db.get_comporable_markets_batch(event_ids, limit=5)

        for i, markets in enumerate(batch_results):
            logging.info(f"Results for {event_ids[i]}: {len(markets)} markets")
            logging.info(markets)

if __name__ == "__main__":
    test_select()