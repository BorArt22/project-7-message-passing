from kafka import KafkaProducer
from kafka.errors import KafkaError
import logging
import os

logging.basicConfig(level=logging.INFO)

KAFKA_HOST = os.environ["KAFKA_HOST"]
KAFKA_TOPIC = os.environ["KAFKA_TOPIC_TEST"]

KAFKA_HOST = str(f'{KAFKA_HOST}')
print("KAFKA HOST",KAFKA_HOST)

class Producer:
    def __init__(self):
        self._init_kafka_producer()

    def _init_kafka_producer(self):
        self.kafka_host = KAFKA_HOST
        self.kafka_topic = KAFKA_TOPIC
        self.producer = KafkaProducer(bootstrap_servers=self.kafka_host)

    def publish_to_kafka(self, message):
        try:
            self.producer.send(self.kafka_topic, message)
            self.producer.flush()
        except KafkaError as ex:
            logging.error(f"Exception {ex}")
        else:
            logging.info(f"Published message {message} into topic {self.kafka_topic}")

if __name__ == "__main__":
    producer = Producer()
    producer.publish_to_kafka(b'Test Message!!!')