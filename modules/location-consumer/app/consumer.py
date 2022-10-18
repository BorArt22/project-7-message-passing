from kafka import KafkaConsumer

TOPIC_NAME = 'test'
KAFKA_SERVER = 'kafka-service.kafka.svc.cluster.local:9092'

consumer = KafkaConsumer(TOPIC_NAME,bootstrap_servers=KAFKA_SERVER)
for message in consumer:
    print (message)