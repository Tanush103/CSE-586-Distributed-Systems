import websockets
import asyncio
import json

#async def producer():
#    return await asyncio.get_event_loop().run_in_executor(None, lambda: input("Enter choice of movie:- Action, Comedy, Crime, Drama"))

async def listen():
    url = "ws://127.0.0.1:8080"

    async with websockets.connect(url) as ws:
        #await ws.send("Hello Server")
        #await ws.send(json.dumps([json.dumps({'topic': await asyncio.get_event_loop().run_in_executor(None, lambda: input("Enter choice of movie:- Action, Comedy, Crime, Drama"))})]))
        await ws.send(json.dumps({'topic': await asyncio.get_event_loop().run_in_executor(None, lambda: input("Enter choice of movie:- Action, Comedy, Crime, Drama"))}))

        while True:
            #msg = await ws.recv()
            #print(msg)

            # Get user input
            # msg = input("Enter something: ")
            #msg = await producer()

            # Send message to the server
            #await ws.send(msg)
            #print(f"> {msg}")

            # Get feedback from server
            feedback = await ws.recv()
            print(f"< {feedback}")

asyncio.get_event_loop().run_until_complete(listen())