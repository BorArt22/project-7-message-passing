# Deploying a Kafka Broker

We create a kafka.yaml file with the following contents, be we replace <ZOOKEEPER-INTERNAL-IP> with the CLUSTER-IP from the Zookeeper ip ('kubectl get services -n kafka'). The broker will fail to deploy if this step is not taken.

'''
apiVersion: v1
kind: Service
metadata:
  labels:
    app: kafka-broker
  name: kafka-service
  namespace: kafka
spec:
  ports:
  - port: 9092
  selector:
    app: kafka-broker
---
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: kafka-broker
  name: kafka-broker
  namespace: kafka
spec:
  replicas: 1
  selector:
    matchLabels:
      app: kafka-broker
  template:
    metadata:
      labels:
        app: kafka-broker
    spec:
      hostname: kafka-broker
      containers:
      - env:
        - name: KAFKA_BROKER_ID
          value: "1"
        - name: KAFKA_ZOOKEEPER_CONNECT
          value: <ZOOKEEPER-INTERNAL-IP>:2181
        - name: KAFKA_LISTENERS
          value: PLAINTEXT://:9092
        - name: KAFKA_ADVERTISED_LISTENERS
          value: PLAINTEXT://kafka-broker:9092
        image: wurstmeister/kafka
        imagePullPolicy: IfNotPresent
        name: kafka-broker
        ports:
        - containerPort: 9092
'''
Again, we are creating two resources — service and deployment — for a single Kafka Broker. We run kubectl apply -f kafka.yaml. We verify this by seeing the pods in our namespace.

# Creating a Kafka Topic

Steps to create topic via commandline : (assumed zookeeper running on port 2181 and kafka server on 9092)

Get inside the kafka pod by using this command
kubectl exec -it kafka-pod-name -- /bin/bash

Create the topic by using below command
kafka-topics.sh --bootstrap-server localhost:9092 --create --topic <topic-name> --replication-factor 1 --partitions 3

you can verify the message produce and consume using below commands-
a) produce-->
kafka-console-producer.sh --broker-list localhost:9092 --topic <topic-you-created-before>

provide some message
b) consume--> 
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic <topic-you-created-before> --from-beginning

you can see the message(provided by producer) here