import logging
import random
import faker
from datetime import datetime

import grpc
import location_pb2
import location_pb2_grpc

logging.basicConfig(level=logging.INFO)

channel = grpc.insecure_channel("localhost:5021")
stub = location_pb2_grpc.LocationServiceStub(channel)

fake = faker.Faker()

person_id = [1, 5, 6, 8, 9]
def random_person():
    return random.choice(person_id)

def random_float():
    return fake.pyfloat(min_value=-1, max_value=1)

location_value = location_pb2.LocationMessage(
    person_id=random_person(), 
    latitude=str(90*random_float()), 
    longitude=str(180*random_float()),
    creation_time=datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')
)

logging.info(f"Sending data {location_value} to gRPC server")
response = stub.Create(location_value)
logging.info(f"Response from gRPC server: {response}")