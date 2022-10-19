import logging
import os
import json
from concurrent import futures

from kafka import KafkaProducer
from kafka.errors import KafkaError

import grpc
import location_pb2
import location_pb2_grpc

logging.basicConfig(level=logging.INFO)

KAFKA_HOST = os.environ["KAFKA_HOST"]
KAFKA_TOPIC = os.environ["KAFKA_TOPIC_LOCATION"]

producer = KafkaProducer(bootstrap_servers=[KAFKA_HOST])

def publish_to_kafka(message):
    try:
        encoded_message = json.dumps(message).encode('utf-8')
        producer.send(KAFKA_TOPIC, message)
        producer.flush()
        logging.info(f"Published message {message} into topic {KAFKA_TOPIC} succesefully")
    except KafkaError as ex:
        logging.error(f"Exception {ex} when published message {message} into topic {KAFKA_TOPIC}")

class LocationServicer(location_pb2_grpc.LocationServiceServicer):
    def Create(self, request, context):
        location_value = {
            "person_id": int(request.person_id),
            "latitude": request.latitude,
            "longitude": request.longitude
        }
        publish_to_kafka(location_value)
        return location_pb2.LocationMessage(**location_value)

# Intiialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
location_pb2_grpc.add_LocationServiceServicer_to_server(LocationServicer(), server)

logging.info(f"Startin gRPC server on 5021...")
server.add_insecure_port("[::]:5021")
server.start()
logging.info(f"gRPC server starts on 5021...")

# Keep thread alive
server.wait_for_termination()

