from configs.csets import settings
from confluent_kafka import Consumer

kafka_instance= settings.KAFKA_INSTANCE

def getConfluentConsumer():
    c = Consumer({
        'bootstrap.servers': kafka_instance,
        'group.id': 'mega_main',
        'auto.offset.reset': 'earliest'
    })

    return c
