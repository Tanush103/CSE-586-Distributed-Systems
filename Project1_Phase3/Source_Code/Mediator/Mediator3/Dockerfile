FROM python:3.7

RUN pip install websockets pymongo[srv] certifi asyncio Flask

ADD getMongo.py /mediator3/
ADD mediator.py /mediator3/

#RUN pip install -r requirements.txt
#RUN python -u server/getMongo.py
#RUN python -u server/mediator.py
WORKDIR /mediator3/
EXPOSE 8080:7000 