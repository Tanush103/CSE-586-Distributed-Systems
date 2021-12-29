from kafka import KafkaConsumer
import  json
print("consumer connection started")
consumer = KafkaConsumer(bootstrap_servers=['127.0.0.1:9092','127.0.0.1:9093','127.0.0.1:9094','127.0.0.1:9095'],auto_offset_reset = 'earliest',value_deserializer = lambda m: json.loads(m.decode('ascii')))
print("consumer connected")
consumer.subscribe(topics=['test_topic'])
print("Subscription Successful")
#print(consumer)
for message in consumer:
    print(message.value)