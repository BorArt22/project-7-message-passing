from kafka import KafkaProducer
from kafka.errors import KafkaError
import logging

logging.basicConfig(level=logging.INFO)


class Producer:
    def __init__(self):
        self._init_kafka_producer()

    def _init_kafka_producer(self):
        self.kafka_host = 'kafka-service.kafka.svc.cluster.local:9092'
        self.kafka_topic = 'test'
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