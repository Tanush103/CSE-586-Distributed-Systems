FROM python:3.7



RUN pip install Flask kafka-python



ADD subscriber.py /subscriber/
ADD templates/index1.html /subscriber/templates/
ADD static/styles.css /subscriber/static/
ADD static/goodfellas.jpg /subscriber/static/
ADD static/johnwick2.jpg /subscriber/static/
ADD static/spotlight.jpg /subscriber/static/
ADD static/thehangover.jpg /subscriber/static/
ADD static/lotr.jpeg /subscriber/static/
ADD static/dark_waters-eclipse-900x0-c-default.jpg /subscriber/static/
ADD static/high-school-musical-the-musical-the-series-movie-poster-md.jpg /subscriber/static/
ADD static/terminator-dark-fate-poster_1565974186.jpg /subscriber/static/
ADD static/junglecruise.jpeg /subscriber/static/
ADD static/we-are-family-movie-poster-2016-1020775866.jpg /subscriber/static/
ADD static/lalaland.jpeg /subscriber/static/
ADD static/dune.jpeg /subscriber/static/



#RUN python -u client/subscriber.py
WORKDIR /subscriber/
