FROM python:3.6
ADD . /DS
WORKDIR /DS

RUN pip install -r requirements.txt
RUN python subscriber.py

EXPOSE 8080
CMD ["python", "Publisher"]