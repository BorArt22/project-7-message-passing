from kafka import KafkaConsumer
import logging
import os

logging.basicConfig(level=logging.INFO)

KAFKA_HOST = os.environ["KAFKA_HOST"]
KAFKA_TOPIC = os.environ["KAFKA_TOPIC_TEST"]

KAFKA_HOST = str(f'{KAFKA_HOST}')
print("KAFKA HOST",KAFKA_HOST)

class Consumer:

    def __init__(self):
        self._init_kafka_consumer()

    def _init_kafka_consumer(self):
        self.kafka_host = KAFKA_HOST
        self.kafka_topic = KAFKA_TOPIC
        self.consumer = KafkaConsumer(
            self.kafka_topic,
            bootstrap_servers=self.kafka_host,
        )

    def consume_from_kafka(self):
        for message in self.consumer:
            logging.info(message.value)


if __name__ == "__main__":

    consumer = Consumer()

    while True:
        consumer.consume_from_kafka()



