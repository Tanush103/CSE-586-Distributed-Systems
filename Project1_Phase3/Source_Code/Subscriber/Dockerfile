FROM python:3.7



RUN pip install websockets pymongo[srv] certifi Flask



ADD subscriber.py /subscriber/
ADD templates/index.html /subscriber/templates/


#RUN python -u client/subscriber.py
WORKDIR /subscriber/
