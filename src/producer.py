import os
import time
import random
from kafka import KafkaProducer
from kafka.errors import KafkaError
from dotenv import load_dotenv
from src.utils import generate_realistic_vitals, generate_anomalous_vitals

load_dotenv()

OUTPUT_TOPIC = os.getenv('OUTPUT_TOPIC')
BOOTSTRAP_SERVERS = os.getenv('BOOTSTRAP_SERVERS')
SASL_USERNAME = os.getenv('SASL_USERNAME')
SASL_PASSWORD = os.getenv('SASL_PASSWORD')
SECURITY_PROTOCOL = os.getenv('SECURITY_PROTOCOL')
SASL_MECHANISM = os.getenv('SASL_MECHANISM')
INTERVAL_MS = int(os.getenv('INTERVAL_MS'))

def create_producer():
    producer = KafkaProducer(
        bootstrap_servers=BOOTSTRAP_SERVERS,
        sasl_plain_username=SASL_USERNAME,
        sasl_plain_password=SASL_PASSWORD,
        security_protocol=SECURITY_PROTOCOL,
        sasl_mechanism=SASL_MECHANISM,
        value_serializer=lambda v: str(v).encode('utf-8')
    )
    return producer

def on_send_success(record_metadata):
    print(f'Successfully sent message to topic: {record_metadata.topic}\n'
          f'Partition: {record_metadata.partition}\n'
          f'Offset: {record_metadata.offset}\n')

def on_send_error(excp):
    print(f'Error sending message: {excp}')

def main():
    producer = create_producer()

    while True:
        # Randomly decide whether to generate realistic or anomalous vitals
        if random.random() < 0.1:  # 10% chance of generating anomalous vitals
            vitals = generate_anomalous_vitals()
            print("Generated anomalous vitals")
        else:
            vitals = generate_realistic_vitals()

        producer.send(OUTPUT_TOPIC, vitals).add_callback(on_send_success).add_errback(on_send_error)
        time.sleep(INTERVAL_MS / 1000)

if __name__ == '__main__':
    main()