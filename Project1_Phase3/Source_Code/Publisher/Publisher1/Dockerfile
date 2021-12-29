FROM python:3.6
ADD . /DS
WORKDIR /DS

RUN pip install -r requirements.txt
#RUN python Publisher.py

EXPOSE 1433
CMD ["python", "Publisher"]