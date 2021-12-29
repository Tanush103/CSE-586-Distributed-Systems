FROM openjdk:11
WORKDIR /server
COPY Server.java .
RUN javac Server.java
EXPOSE 1433
CMD ["java", "Server"]