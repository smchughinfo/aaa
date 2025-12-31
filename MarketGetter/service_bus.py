from azure.servicebus import ServiceBusClient, ServiceBusMessage
import os
import config
import json
import logging

def queue_message(event_ids):
    with ServiceBusClient.from_connection_string(config.aaa_sb_aaa_connection_string) as client:
        with client.get_queue_sender("comparison-queue") as sender:
            text = json.dumps(event_ids)
            message = ServiceBusMessage(text)
            sender.send_messages(message)
            logging.info(f"Service Bus Message sent! {text}")

################################################################################################
####### MAIN ###################################################################################
################################################################################################

def test_service_bus():
    queue_message(['134117', '134115', '134114', '134120', 'KXBTC15M-25DEC302200', 'KXETH15M-25DEC302200'])
    logging.info("TEST SB")

if __name__ == "__main__":
    test_service_bus()