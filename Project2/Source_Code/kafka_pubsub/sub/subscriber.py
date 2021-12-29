from flask.wrappers import Request

import json
from flask import Flask, render_template,Response,request
from kafka import KafkaConsumer



app = Flask(__name__)

#async def producer():
#    return await asyncio.get_event_loop().run_in_executor(None, lambda: input("Enter choice of movie:- Action, Comedy, Crime, Drama"))
@app.route('/', methods=['POST','GET'])
def index():
    return render_template('index1.html')


@app.route('/subAction',methods=["POST","GET"])
def callbackaction():
    
    #list1=[]
    #consumer = KafkaConsumer(bootstrap_servers=['127.0.0.1:9092','127.0.0.1:9093','127.0.0.1:9094','127.0.0.1:9095'],auto_offset_reset = 'earliest',value_deserializer = lambda m: json.loads(m.decode('ascii')))
    consumer = KafkaConsumer(bootstrap_servers=['kafka1:19092','kafka2:19093','kafka3:19094','kafka4:19095'],api_version=(0,11,5),auto_offset_reset = 'earliest',value_deserializer = lambda m: json.loads(m.decode('ascii')))

    consumer.subscribe(topics=['action'])
    
    print("You have been subscribed to Action Movies")
    for message in consumer:
    #    #list1.append(message.value)
        print(message.value)
        
    return '<a>Movies List</a>' %(message.value)
        

    

@app.route('/subComedy')
def callbackcomedy():
    #consumer = KafkaConsumer(bootstrap_servers=['127.0.0.1:9092','127.0.0.1:9093','127.0.0.1:9094','127.0.0.1:9095'],auto_offset_reset = 'earliest',value_deserializer = lambda m: json.loads(m.decode('ascii')))
    #consumer = KafkaConsumer(bootstrap_servers=['172.20.0.1:9092','172.20.0.1:9093','172.20.0.1:9094','172.20.0.1:9095'],auto_offset_reset = 'earliest',value_deserializer = lambda m: json.loads(m.decode('ascii')))
    consumer = KafkaConsumer(bootstrap_servers=['kafka1:19092','kafka2:19093','kafka3:19094','kafka4:19095'],api_version=(0,11,5),auto_offset_reset = 'earliest',value_deserializer = lambda m: json.loads(m.decode('ascii')))
    print("connected")
    consumer.subscribe(topics=['comedy'])

    print("You have been subscribed to Comedy Movies")
    
    
    
    
    for message in consumer:
        print(message.value)
    

@app.route('/subCrime')
def callbackcrime():
    #consumer = KafkaConsumer(bootstrap_servers=['127.0.0.1:9092','127.0.0.1:9093','127.0.0.1:9094','127.0.0.1:9095'],auto_offset_reset = 'earliest',value_deserializer = lambda m: json.loads(m.decode('ascii')))
    #consumer = KafkaConsumer(bootstrap_servers=['172.20.0.1:9092','172.20.0.1:9093','172.20.0.1:9094','172.20.0.1:9095'],auto_offset_reset = 'earliest',value_deserializer = lambda m: json.loads(m.decode('ascii')))
    consumer = KafkaConsumer(bootstrap_servers=['kafka1:19092','kafka2:19093','kafka3:19094','kafka4:19095'],api_version=(0,11,5),auto_offset_reset = 'earliest',value_deserializer = lambda m: json.loads(m.decode('ascii')))

    consumer.subscribe(topics=['crime'])

    print("You have been subscribed to Crime Movies")
    
    
    for message in consumer:
        print(message.value)
    return '<a>Movies List</a>' %(message.value)
@app.route('/subDrama')
def callbackdrama():
    #consumer = KafkaConsumer(bootstrap_servers=['127.0.0.1:9092','127.0.0.1:9093','127.0.0.1:9094','127.0.0.1:9095'],auto_offset_reset = 'earliest',value_deserializer = lambda m: json.loads(m.decode('ascii')))
    #consumer = KafkaConsumer(bootstrap_servers=['172.20.0.1:9092','172.20.0.1:9093','172.20.0.1:9094','172.20.0.1:9095'],auto_offset_reset = 'earliest',value_deserializer = lambda m: json.loads(m.decode('ascii')))
    consumer = KafkaConsumer(bootstrap_servers=['kafka1:19092','kafka2:19093','kafka3:19094','kafka4:19095'],api_version=(0,11,5),auto_offset_reset = 'earliest',value_deserializer = lambda m: json.loads(m.decode('ascii')))

    consumer.subscribe(topics=['drama'])
    print("You have been subscribed to Drama Movies")
    
    for message in consumer:
        print(message.value)
    return '<a>Movies List</a>' %(message.value)

@app.route('/subSciFi',methods=["POST","GET"])
def callbackscifi():
    
    list1=[]
    #consumer = KafkaConsumer(bootstrap_servers=['127.0.0.1:9092','127.0.0.1:9093','127.0.0.1:9094','127.0.0.1:9095'],auto_offset_reset = 'earliest',value_deserializer = lambda m: json.loads(m.decode('ascii')))
    consumer = KafkaConsumer(bootstrap_servers=['kafka1:19092','kafka2:19093','kafka3:19094','kafka4:19095'],api_version=(0,11,5),auto_offset_reset = 'earliest',value_deserializer = lambda m: json.loads(m.decode('ascii')))

    consumer.subscribe(topics=['scifi'])
    print("You have been subscribed to Sci-Fi Movies")
    
    
    for message in consumer:
        #list1.append(message.value)
        print(message.value)
        
    return '<a>Movies List</a>' %(message.value)
        

    

@app.route('/subAdventure')
def callbackadventure():
    #consumer = KafkaConsumer(bootstrap_servers=['127.0.0.1:9092','127.0.0.1:9093','127.0.0.1:9094','127.0.0.1:9095'],auto_offset_reset = 'earliest',value_deserializer = lambda m: json.loads(m.decode('ascii')))
    #consumer = KafkaConsumer(bootstrap_servers=['172.20.0.1:9092','172.20.0.1:9093','172.20.0.1:9094','172.20.0.1:9095'],auto_offset_reset = 'earliest',value_deserializer = lambda m: json.loads(m.decode('ascii')))
    consumer = KafkaConsumer(bootstrap_servers=['kafka1:19092','kafka2:19093','kafka3:19094','kafka4:19095'],api_version=(0,11,5),auto_offset_reset = 'earliest',value_deserializer = lambda m: json.loads(m.decode('ascii')))

    consumer.subscribe(topics=['adventure'])
    print("You have been subscribed to Adventure Movies")
    
    for message in consumer:
        print(message.value)
    return '<a>Movies List</a>' %(message.value)

@app.route('/subFantasy')
def callbackfantasy():
    #consumer = KafkaConsumer(bootstrap_servers=['127.0.0.1:9092','127.0.0.1:9093','127.0.0.1:9094','127.0.0.1:9095'],auto_offset_reset = 'earliest',value_deserializer = lambda m: json.loads(m.decode('ascii')))
    #consumer = KafkaConsumer(bootstrap_servers=['172.20.0.1:9092','172.20.0.1:9093','172.20.0.1:9094','172.20.0.1:9095'],auto_offset_reset = 'earliest',value_deserializer = lambda m: json.loads(m.decode('ascii')))
    consumer = KafkaConsumer(bootstrap_servers=['kafka1:19092','kafka2:19093','kafka3:19094','kafka4:19095'],api_version=(0,11,5),auto_offset_reset = 'earliest',value_deserializer = lambda m: json.loads(m.decode('ascii')))

    consumer.subscribe(topics=['fantasy'])
    print("You have been subscribed to Fantasy Movies")
    
    
    for message in consumer:
        print(message.value)
    return '<a>Movies List</a>' %(message.value)

@app.route('/subFamily')
def callbackfamily():
    #consumer = KafkaConsumer(bootstrap_servers=['127.0.0.1:9092','127.0.0.1:9093','127.0.0.1:9094','127.0.0.1:9095'],auto_offset_reset = 'earliest',value_deserializer = lambda m: json.loads(m.decode('ascii')))
    #consumer = KafkaConsumer(bootstrap_servers=['172.20.0.1:9092','172.20.0.1:9093','172.20.0.1:9094','172.20.0.1:9095'],auto_offset_reset = 'earliest',value_deserializer = lambda m: json.loads(m.decode('ascii')))
    consumer = KafkaConsumer(bootstrap_servers=['kafka1:19092','kafka2:19093','kafka3:19094','kafka4:19095'],api_version=(0,11,5),auto_offset_reset = 'earliest',value_deserializer = lambda m: json.loads(m.decode('ascii')))

    consumer.subscribe(topics=['family'])
    print("You have been subscribed to Family Movies")
    
    for message in consumer:
        print(message.value)
    return '<a>Movies List</a>' %(message.value)

@app.route('/subMusical')
def callbackmusical():
    #consumer = KafkaConsumer(bootstrap_servers=['127.0.0.1:9092','127.0.0.1:9093','127.0.0.1:9094','127.0.0.1:9095'],auto_offset_reset = 'earliest',value_deserializer = lambda m: json.loads(m.decode('ascii')))
    #consumer = KafkaConsumer(bootstrap_servers=['172.20.0.1:9092','172.20.0.1:9093','172.20.0.1:9094','172.20.0.1:9095'],auto_offset_reset = 'earliest',value_deserializer = lambda m: json.loads(m.decode('ascii')))
    consumer = KafkaConsumer(bootstrap_servers=['kafka1:19092','kafka2:19093','kafka3:19094','kafka4:19095'],api_version=(0,11,5),auto_offset_reset = 'earliest',value_deserializer = lambda m: json.loads(m.decode('ascii')))

    consumer.subscribe(topics=['musical'])
    print("You have been subscribed to Musical Movies")
    
    
    for message in consumer:
        print(message.value)
    return '<a>Movies List</a>' %(message.value)

@app.route('/subThriller')
def callbackthriller():
    #consumer = KafkaConsumer(bootstrap_servers=['127.0.0.1:9092','127.0.0.1:9093','127.0.0.1:9094','127.0.0.1:9095'],auto_offset_reset = 'earliest',value_deserializer = lambda m: json.loads(m.decode('ascii')))
    #consumer = KafkaConsumer(bootstrap_servers=['172.20.0.1:9092','172.20.0.1:9093','172.20.0.1:9094','172.20.0.1:9095'],auto_offset_reset = 'earliest',value_deserializer = lambda m: json.loads(m.decode('ascii')))
    consumer = KafkaConsumer(bootstrap_servers=['kafka1:19092','kafka2:19093','kafka3:19094','kafka4:19095'],api_version=(0,11,5),auto_offset_reset = 'earliest',value_deserializer = lambda m: json.loads(m.decode('ascii')))

    consumer.subscribe(topics=['thriller'])
    print("You have been subscribed to Thriller Movies")
    
    
    for message in consumer:
        print(message.value)
    return '<a>Movies List</a>' %(message.value)

@app.route('/subActionSciFi')
def callbackactionscifi():
    #consumer = KafkaConsumer(bootstrap_servers=['127.0.0.1:9092','127.0.0.1:9093','127.0.0.1:9094','127.0.0.1:9095'],auto_offset_reset = 'earliest',value_deserializer = lambda m: json.loads(m.decode('ascii')))
    #consumer = KafkaConsumer(bootstrap_servers=['172.20.0.1:9092','172.20.0.1:9093','172.20.0.1:9094','172.20.0.1:9095'],auto_offset_reset = 'earliest',value_deserializer = lambda m: json.loads(m.decode('ascii')))
    consumer = KafkaConsumer(bootstrap_servers=['kafka1:19092','kafka2:19093','kafka3:19094','kafka4:19095'],api_version=(0,11,5),auto_offset_reset = 'earliest',value_deserializer = lambda m: json.loads(m.decode('ascii')))

    consumer.subscribe(topics=['action','scifi'])
    print("You have been subscribed to Action and SciFi Movies")
    
    
    for message in consumer:
        print(message.value)
    return '<a>Movies List</a>' %(message.value)

@app.route('/subMusicalDrama')
def callbackmusicaldrama():
    #consumer = KafkaConsumer(bootstrap_servers=['127.0.0.1:9092','127.0.0.1:9093','127.0.0.1:9094','127.0.0.1:9095'],auto_offset_reset = 'earliest',value_deserializer = lambda m: json.loads(m.decode('ascii')))
    #consumer = KafkaConsumer(bootstrap_servers=['172.20.0.1:9092','172.20.0.1:9093','172.20.0.1:9094','172.20.0.1:9095'],auto_offset_reset = 'earliest',value_deserializer = lambda m: json.loads(m.decode('ascii')))
    consumer = KafkaConsumer(bootstrap_servers=['kafka1:19092','kafka2:19093','kafka3:19094','kafka4:19095'],api_version=(0,11,5),auto_offset_reset = 'earliest',value_deserializer = lambda m: json.loads(m.decode('ascii')))

    consumer.subscribe(topics=['musical','drama'])
    print("You have been subscribed to Musical and Drama Movies")
    
    
    for message in consumer:
        print(message.value)
    return '<a>Movies List</a>' %(message.value)


        

    



if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000,debug=True)
