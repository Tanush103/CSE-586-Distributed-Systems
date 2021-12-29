FROM python:3.7

RUN pip install websockets pymongo[srv] certifi asyncio Flask

ADD getMongo.py /mediator/
ADD mediator.py /mediator/

#RUN pip install -r requirements.txt
#RUN python -u server/getMongo.py
#RUN python -u server/mediator.py
WORKDIR /mediator/
EXPOSE 8080:8080