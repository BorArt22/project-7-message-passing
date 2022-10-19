from kafka import KafkaConsumer
import logging
import os

logging.basicConfig(level=logging.INFO)

KAFKA_HOST = os.environ["KAFKA_HOST"]
KAFKA_TOPIC = os.environ["KAFKA_TOPIC_TEST"]

class Consumer:

    def __init__(self):
        self._init_kafka_consumer()

    def _init_kafka_consumer(self):
        self.consumer = KafkaConsumer(
            KAFKA_TOPIC,
            bootstrap_servers=[KAFKA_HOST],
        )

    def consume_from_kafka(self):
        for message in self.consumer:
            logging.info(message.value)


if __name__ == "__main__":

    consumer = Consumer()

    while True:
        consumer.consume_from_kafka()



