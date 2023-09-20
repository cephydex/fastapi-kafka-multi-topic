from aiokafka import (
    # KafkaConsumer,
    TopicPartition,
    ConsumerRecord,
)
from configs.clog import LOGGER
import asyncio
from .utils import ( getConfluentConsumer )
from typing import (
    Callable,
)
from parse import *


def consume_general(topic: str, callback: Callable):
    consumer = getConfluentConsumer()
    consumer.subscribe([topic])

    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                LOGGER.info("No message found!")
                continue

            if msg.error():
                LOGGER.error(msg.error())
                continue
            # else:
            topic, key, value = parse(msg)
            callback(topic, key, value)
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()

def parse_message(topic: str, key: str, value: str):
    LOGGER.info(f"Consumed message with topic={topic}, key={key}, value={value}")


def consumeMultiple():
    consumer = getConfluentConsumer()
    consumer.subscribe(['my_topic','my_topic2'])

    while True:
        event = consumer.poll(1.0)
        if event is None:
            LOGGER.info("No message received")
            continue
        if event.error():
            raise Exception(event.error())
        
        val = event.value().decode('utf8')
        partition = event.partition()
        print(f'Received: {val} from partition {partition} and topic: {event.topic()}')
        LOGGER.info(f'Received: {val} from partition {partition} and topic: {event.topic()}')
        consumer.commit(event)

async def consume_all():
    # consume_general('my_topic', parse_message)
    consumeMultiple(parse_message)
    pass