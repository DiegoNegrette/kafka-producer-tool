import json
import os

from kafka import KafkaProducer

bootstrap_servers = os.getenv('KAFKA_BOOTSTRAP_SERVER', 'kafka:9092')  # Default to 'kafka:9092'

producer = KafkaProducer(
    bootstrap_servers=bootstrap_servers,  # Use 'kafka' since it's defined in Docker Compose
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    key_serializer=lambda k: json.dumps(k).encode('utf-8')
)

def send_message(topic, key, value):
    # Ensure key and value are JSON serializable
    producer.send(topic, key=key, value=value)
    producer.flush()
