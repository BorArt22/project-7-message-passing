from kafka import KafkaConsumer
import logging
import os
from services import LocationService
from models import Location


logging.basicConfig(level=logging.INFO)

KAFKA_HOST = os.environ["KAFKA_HOST"]
KAFKA_TOPIC = os.environ["KAFKA_TOPIC_LOCATION"]

consumer = KafkaConsumer(KAFKA_TOPIC, bootstrap_servers=[KAFKA_HOST])


while True:
    for message in consumer:
        location_data = message.value.decode('utf-8')
        logging.info(f"Consumed message {location_data} from topic {KAFKA_TOPIC} succesefully")
        location: Location = LocationService.create(location_value)
        logging.info(f"Consumed message succesefully inserted to database")



