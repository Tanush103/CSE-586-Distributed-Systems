from typing import Collection
import websockets
import asyncio
import pymongo
from pymongo import MongoClient
import certifi
from pymongo.message import update
import json
from getMongo import getMovies

PORT = 8080

#print("Mediator Server listening on port "+ str(PORT))

connected = set()

ca = certifi.where()

cluster = pymongo.MongoClient("mongodb+srv://rishi:rishi@cluster0.sn3xi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",tlsCAFile=ca)

db = cluster["Movies"]
collection = db["Subs"]

async def echo(websocket, path):
    print("A subscriber just connected")
    connected.add(websocket)

    #if(connected):
    #    print()

    try:
        async for  message in websocket:
            print("Received subscription from subscriber: "+ message)
            #print(message)
            #print(type(message))
            dict=json.loads(message)
            #print(type(dict))
            collection.insert_one(dict)
            #await websocket.send("Pong: "+message

            #await connected.send("Movies based on your interests : "+ getMovies.final_list)

            #Iterate over all the sockets in the connected set
            for conn in connected:
                #if conn is websocket:
                await conn.send(getMovies())

    except websockets.exceptions.ConnectionClosed as e:
        print("Subscriber disconnected!")
print("Mediator Server listening on port "+ str(PORT))
start_server = websockets.serve(echo, "0.0.0.0", PORT)
#print("Mediator Server listening on port "+ str(PORT))
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()