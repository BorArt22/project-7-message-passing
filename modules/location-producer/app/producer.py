from kafka import KafkaProducer


TOPIC_NAME = 'test'
KAFKA_SERVER = 'kafka-service.kafka.svc.cluster.local:9092'

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

producer.send(TOPIC_NAME, b'Test Message!!!')
producer.flush()