FROM python:3.7

RUN pip install websockets pymongo[srv] certifi asyncio Flask

ADD getMongo.py /mediator2/
ADD mediator.py /mediator2/

#RUN pip install -r requirements.txt
#RUN python -u server/getMongo.py
#RUN python -u server/mediator.py
WORKDIR /mediator2/
EXPOSE 8080:7000