FROM python:3.6


WORKDIR /publisher

RUN pip install imdbpy kafka-python
#RUN python Publisher.py
ADD getData.py /publisher/
ADD publisher.py /publisher/
ADD test.csv /publisher/


