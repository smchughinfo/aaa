from azure.servicebus import ServiceBusClient, ServiceBusMessage
import os
import config

def queue_message(event_ids):
    with ServiceBusClient.from_connection_string(config.aaa_sb_aaa_connection_string) as client:
        with client.get_queue_sender("comparison-queue") as sender:
            message = ServiceBusMessage("Hello from Python!")
            sender.send_messages(message)
            print("Message sent!")

def test_service_bus():
    
    print("TEST SB")

if __name__ == "__main__":
    test_service_bus()