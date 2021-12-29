import websockets
import asyncio
import json
from flask import Flask, render_template, request


async def listen(input):
    url = "ws://172.20.0.1:8080"

    async with websockets.connect(url) as ws:
        #await ws.send("Hello Server")
        #await ws.send(json.dumps([json.dumps({'topic': await asyncio.get_event_loop().run_in_executor(None, lambda: input("Enter choice of movie:- Action, Comedy, Crime, Drama"))})]))
        await ws.send(json.dumps({'topic': await asyncio.get_event_loop().run_in_executor(None, lambda: input)}))

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
            return feedback





app = Flask(__name__)

#async def producer():
#    return await asyncio.get_event_loop().run_in_executor(None, lambda: input("Enter choice of movie:- Action, Comedy, Crime, Drama"))
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/subAction')
def callbackaction():
    print("called")
    movie = "Action"
    #last_name = request.form['last_name']
    'You have been subscribed to %s movies</a>' % (movie)
    try:
        asyncio.get_event_loop().run_until_complete(listen(movie))
    except RuntimeError as ex:
        #if "There is no current event loop in thread" in str(ex):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        asyncio.get_event_loop().run_until_complete(listen(movie))


    return 'You have been subscribed to %s movies</a>' % (movie)

    #asyncio.get_event_loop().run_until_complete(listen(movie))
    
@app.route('/subComedy')
def callbackcomedy():
    movie = "Comedy"
    #last_name = request.form['last_name']
    
    try:
        return asyncio.get_event_loop().run_until_complete(listen(movie))
    except RuntimeError as ex:
        if "There is no current event loop in thread" in str(ex):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            return asyncio.get_event_loop().run_until_complete(listen(movie))

    
    

    #asyncio.get_event_loop().run_until_complete(listen(movie))
    return 'You have been subscribed to %s movies</a>' % (movie)
@app.route('/subCrime')
def callbackcrime():
    movie = "Crime"
    #last_name = request.form['last_name']
    
    try:
        return asyncio.get_event_loop().run_until_complete(listen(movie))
    except RuntimeError as ex:
        if "There is no current event loop in thread" in str(ex):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            return asyncio.get_event_loop().run_until_complete(listen(movie))

    
    

    #asyncio.get_event_loop().run_until_complete(listen(movie))
    return 'You have been subscribed to %s movies</a>' % (movie)
@app.route('/subDrama')
def callbackdrama():
    movie = "Drama"
    #last_name = request.form['last_name']
    
    try:
        return asyncio.get_event_loop().run_until_complete(listen(movie))
    except RuntimeError as ex:
        if "There is no current event loop in thread" in str(ex):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            return asyncio.get_event_loop().run_until_complete(listen(movie))

    
    

    #asyncio.get_event_loop().run_until_complete(listen(movie))
    return 'You have been subscribed to %s movies</a>' % (movie)



if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000,debug=True,use_reloader=False)
