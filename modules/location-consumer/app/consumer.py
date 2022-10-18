from kafka import KafkaConsumer
import logging
import os

logging.basicConfig(level=logging.INFO)

KAFKA_HOST = os.environ["KAFKA_HOST"]
KAFKA_TOPIC = os.environ["KAFKA_TOPIC_TEST"]

KAFKA_SERVER = KAFKA_HOST
TOPIC_NAME = KAFKA_TOPIC

consumer = KafkaConsumer(TOPIC_NAME,bootstrap_servers=KAFKA_SERVER)
for message in consumer:
    print (message)
    logging.info(f"Consumed message {message} into topic {TOPIC_NAME}")