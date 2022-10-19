import logging
import os
import json

from kafka import KafkaProducer
from kafka.errors import KafkaError

logging.basicConfig(level=logging.INFO)

KAFKA_HOST = os.environ["KAFKA_HOST"]
KAFKA_TOPIC = os.environ["KAFKA_TOPIC_LOCATION"]

producer = KafkaProducer(bootstrap_servers=[KAFKA_HOST])

def publish_to_kafka(message):
    try:
        encoded_message = json.dumps(message).encode('utf-8')
        producer.send(KAFKA_TOPIC, encoded_message)
        producer.flush()
        logging.info(f"Published message {encoded_message} into topic {KAFKA_TOPIC} succesefully")
    except KafkaError as ex:
        logging.error(f"Exception {ex} when published message {message} into topic {KAFKA_TOPIC}")
        