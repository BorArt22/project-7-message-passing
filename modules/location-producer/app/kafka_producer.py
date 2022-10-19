import logging
import os

from kafka import KafkaProducer
from kafka.errors import KafkaError

logging.basicConfig(level=logging.INFO)

KAFKA_HOST = os.environ["KAFKA_HOST"]
KAFKA_TOPIC = os.environ["KAFKA_TOPIC_LOCATION"]

class Producer:
    def __init__(self):
        self._init_kafka_producer()

    def _init_kafka_producer(self):
        self.producer = KafkaProducer(bootstrap_servers=[KAFKA_HOST])

    def publish_to_kafka(self, message):
        try:
            self.producer.send(KAFKA_TOPIC, message)
            self.producer.flush()
        except KafkaError as ex:
            logging.error(f"Exception {ex}")
        else:
            logging.info(f"Published message {message} into topic {KAFKA_TOPIC}")

if __name__ == "__main__":
    producer = Producer()
    producer.publish_to_kafka(b'Test Message!!!')