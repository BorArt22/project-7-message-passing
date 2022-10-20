import os
import logging
import psycopg2

from kafka import KafkaConsumer

from location_service import location_save_to_database

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("udaconnect-location-consumer")

# Connect to kafka
KAFKA_HOST = os.environ["KAFKA_HOST"]
KAFKA_TOPIC = os.environ["KAFKA_TOPIC_LOCATION"]

consumer = KafkaConsumer(KAFKA_TOPIC, bootstrap_servers=[KAFKA_HOST])
logging.info(f"Connected to kafka")

# Connect to database
DB_USERNAME = os.environ["DB_USERNAME"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]
DB_NAME = os.environ["DB_NAME"]

conn = psycopg2.connect(
    database = DB_NAME,
    user = DB_USERNAME,
    password = DB_PASSWORD,
    host = DB_HOST,
    port = DB_PORT
)
cur = conn.cursor()

# reading message from queue
while True:
    for message in consumer:
        logging.info(f"Get message {message}")
        location_data = message.value.decode('utf-8')
        logging.info(f"Consumed message {location_data} from topic {KAFKA_TOPIC} succesefully")
        location_save_to_database(location_data, cur)
        logging.info(f"Consumed message succesefully inserted to database")



