from time import sleep
from kafka import KafkaProducer #Must run "pip install kafka-python"

class Kafka:
    def __init__():
        global producer = KafkaProducer(bootstrap-server=["localhost:9092"]) #Convert to the IP of the Host computer on Deployment

    def sendRecord(message):
        producer.send('test', value = message)
