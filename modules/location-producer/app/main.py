import logging
from concurrent import futures

import grpc
import location_pb2
import location_pb2_grpc

from kafka_producer import publish_to_kafka

logging.basicConfig(level=logging.INFO)

class LocationServicer(location_pb2_grpc.LocationServiceServicer):
    def Create(self, request, context):
        location_value = {
            "person_id": int(request.person_id),
            "latitude": request.latitude,
            "longitude": request.longitude,
            "creation_time": request.creation_time
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

