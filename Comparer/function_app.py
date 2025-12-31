import azure.functions as func
import logging
import json
import main

app = func.FunctionApp()

@app.service_bus_queue_trigger(
    arg_name="azservicebus",
    queue_name="comparison-queue",
    connection="aaa_sb_aaa_connection_string"
)
def process_comparison_queue(azservicebus: func.ServiceBusMessage):
    # hello
    logging.info('Processing comparison queue message')

    # get function data
    message_body = azservicebus.get_body().decode('utf-8')
    logging.info(f'Message body: {message_body}')
    event_ids = json.loads(message_body)
    logging.info(f'Event IDs to process: {event_ids}')

    # run comparer
    main.compare_markets(event_ids)

    # success!
    logging.info('Message processed successfully')