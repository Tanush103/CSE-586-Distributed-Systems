FROM openjdk:11
WORKDIR /client
COPY Client.java .
RUN javac Client.java
EXPOSE 1433
CMD ["java", "Client"]