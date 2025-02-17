import os
from confluent_kafka import Producer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroSerializer
from confluent_kafka.serialization import StringSerializer, SerializationContext, MessageField

# Kafka and Schema Registry configuration
bootstrap_servers = os.getenv('KAFKA_BOOTSTRAP_SERVER', 'kafka:9092')
schema_registry_url = 'http://kafka-schema-registry:8081'

# Initialize Schema Registry Client
schema_registry_client = SchemaRegistryClient({'url': schema_registry_url})

# Define Avro schema
avro_schema_str = """
{
  "type": "record",
  "name": "YourRecord",
  "fields": [
    {"name": "id", "type": "int"},
    {"name": "name", "type": "string"},
    {"name": "timestamp", "type": "string"}
  ]
}
"""

# Create Avro Serializer
avro_serializer = AvroSerializer(
    schema_registry_client, avro_schema_str
)

# String serializer for the key
string_serializer = StringSerializer('utf_8')

# Kafka Producer Configuration
producer_config = {
    'bootstrap.servers': bootstrap_servers,
    'client.id': 'python-producer'
}

producer = Producer(producer_config)

def delivery_report(err, msg):
    if err:
        print("Delivery failed:", err)
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

# Create a message payload
value = {"id": 1, "name": "Alice", "timestamp": "2025-02-17T10:00:00"}

# Serialize message with proper context
avro_value = avro_serializer(
    value, SerializationContext('topic.test', MessageField.VALUE)  # ✅ Corrected
)

# Produce the message
producer.produce(
    topic='topic.test',
    key=string_serializer('my-key'),  # Serialize the key
    value=avro_value,
    callback=delivery_report
)

producer.flush()
