import azure.functions as func
import logging
import json
import config
# Import your comparison logic
import open_ai
from EXPERIMENTAL_SYSTEM_PROMPTS import prompts

app = func.FunctionApp()

@app.service_bus_queue_trigger(
    arg_name="azservicebus",
    queue_name="comparison-queue",  # Your actual queue name
    connection="aaa_sb_aaa_connection_string"  # Reference to app setting
)
def process_comparison_queue(azservicebus: func.ServiceBusMessage):
    """
    Automatically triggered when message arrives in comparison-queue.
    Message is automatically removed from queue when function completes successfully.
    """
    logging.info('Processing comparison queue message')

    # Get message body (it's bytes, so decode to string)
    message_body = azservicebus.get_body().decode('utf-8')
    logging.info(f'Message body: {message_body}')

    try:
        # Parse the JSON (your service_bus.py sends JSON array of event_ids)
        event_ids = json.loads(message_body)
        logging.info(f'Event IDs to process: {event_ids}')

        # TODO: Fetch actual market data from database using event_ids
        # test_data = fetch_market_pairs_from_db(event_ids)

        # For now, placeholder:
        test_data = []  # You'll replace this with real data

        if test_data:
            # Use your best prompt
            prompt = prompts["9"]

            # Run comparisons
            results = open_ai.compare_markets(prompt, test_data)

            logging.info(f'Processed {len(results.comparisons)} comparisons')
            logging.info(f'Found {sum(1 for c in results.comparisons if c.arbitrage_match)} arbitrage opportunities')

            # TODO: Save results to database

        else:
            logging.warning(f'No test data found for event_ids: {event_ids}')

    except json.JSONDecodeError as e:
        logging.error(f'Failed to parse message as JSON: {e}')
        raise  # Re-raise to move message to dead-letter queue

    except Exception as e:
        logging.error(f'Error processing message: {e}')
        raise  # Re-raise to move message to dead-letter queue

    # When function completes successfully, Azure automatically removes message from queue!
    logging.info('Message processed successfully')
