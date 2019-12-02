from kafka import KafkaProducer
import json
from bson import json_util


def on_send_error(excp):
    print(excp)


def on_send_success(excp):
    print(excp)


def insert_kafka(topic, json_data):
    # producer = KafkaProducer(bootstrap_servers=[
    #     'kafka-0-broker.confluent-kafka.autoip.dcos.thisdcos.directory',
    #     'kafka-1-broker.confluent-kafka.autoip.dcos.thisdcos.directory',
    #     'kafka-2-broker.confluent-kafka.autoip.dcos.thisdcos.directory',
    #     'kafka-3-broker.confluent-kafka.autoip.dcos.thisdcos.directory'
    # ], value_serializer=lambda v: json.dumps(v, default=json_util.default).encode('utf-8'))
    producer = KafkaProducer(bootstrap_servers=['192.168.120.85:1025',
                                                '192.168.120.54:1026',
                                                '192.168.120.53:1026',
                                                '192.168.120.88:1025'],
        value_serializer=lambda v: json.dumps(v, default=json_util.default).encode('utf-8'))

    producer.send(topic, json_data).add_callback(on_send_success).add_errback(on_send_error)
    producer.flush()
