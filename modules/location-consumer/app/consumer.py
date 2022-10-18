from kafka import KafkaConsumer
import logging

logging.basicConfig(level=logging.INFO)

TOPIC_NAME = 'test'
KAFKA_SERVER = 'kafka-service.kafka.svc.cluster.local:9092'

consumer = KafkaConsumer(TOPIC_NAME,bootstrap_servers=KAFKA_SERVER)
for message in consumer:
    print (message)
    logging.info(f"Consumed message {message} into topic {TOPIC_NAME}")