# encoding=utf-8


from kafka import KafkaConsumer
import json

bootstrap_servers = {}

consumer = KafkaConsumer('my_test', "10.80.109.21:9092")

consumer.subscribe(['ly_test'])

for msg in consumer:
	print(json.loads(msg.value))
