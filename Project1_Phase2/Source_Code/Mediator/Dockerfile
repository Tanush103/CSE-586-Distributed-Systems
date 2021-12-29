FROM python:latest
ADD . /DS
WORKDIR /DS

RUN pip install -r requirements.txt
RUN python getMongo.py
RUN python mediator.py

EXPOSE 8080
CMD ["python", "mediator.py"]