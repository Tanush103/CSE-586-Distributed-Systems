from kafka import KafkaProducer
import json
from getData import getHindi, getEnglish, getTamil
import time

def json_serializer(data):
    return json.dumps(data).encode("utf-8")

publisher=KafkaProducer(bootstrap_servers=['kafka1:19092','kafka2:19093','kafka3:19094','kafka4:19095'], value_serializer=json_serializer, api_version=(0,11,5))

#actionMovies = getAction()
#comedyMovies = getComedy()
#crimeMovies = getCrime()
#dramaMovies = getDrama()

hindiMovies=getHindi()
englishMovies=getEnglish()
tamilMovies=getTamil()

actionMovies=[]
crimeMovies=[]
dramaMovies=[]
comedyMovies=[]
adventureMovies=[]
fantasyMovies=[]
familyMovies=[]
musicalMovies=[]
scifiMovies=[]
thrillerMovies=[]




for movie in englishMovies:
    if('Action' in movie['genre']):
        actionMovies.append(movie)
    if('Comedy' in movie['genre']):
        comedyMovies.append(movie)
    if('Drama' in movie['genre']):
        dramaMovies.append(movie)
    if('Crime' in movie['genre']):
        crimeMovies.append(movie)
    if('Sci-Fi' in movie['genre']):
        scifiMovies.append(movie)
    if('Adventure' in movie['genre']):
        adventureMovies.append(movie)
    if('Fantasy' in movie['genre']):
        fantasyMovies.append(movie)
    if('Family' in movie['genre']):
        familyMovies.append(movie)
    if('Musical' in movie['genre']):
        musicalMovies.append(movie)
    if('Thriller' in movie['genre']):
        thrillerMovies.append(movie)

for movie in hindiMovies:
    if('Action' in movie['genre']):
        actionMovies.append(movie)
    if('Comedy' in movie['genre']):
        comedyMovies.append(movie)
    if('Drama' in movie['genre']):
        dramaMovies.append(movie)
    if('Crime' in movie['genre']):
        crimeMovies.append(movie)
    if('Sci-Fi' in movie['genre']):
        scifiMovies.append(movie)
    if('Adventure' in movie['genre']):
        adventureMovies.append(movie)
    if('Fantasy' in movie['genre']):
        fantasyMovies.append(movie)
    if('Family' in movie['genre']):
        familyMovies.append(movie)
    if('Musical' in movie['genre']):
        musicalMovies.append(movie)
    if('Thriller' in movie['genre']):
        thrillerMovies.append(movie)

for movie in tamilMovies:
    if('Action' in movie['genre']):
        actionMovies.append(movie)
    if('Comedy' in movie['genre']):
        comedyMovies.append(movie)
    if('Drama' in movie['genre']):
        dramaMovies.append(movie)
    if('Crime' in movie['genre']):
        crimeMovies.append(movie)
    if('Sci-Fi' in movie['genre']):
        scifiMovies.append(movie)
    if('Adventure' in movie['genre']):
        adventureMovies.append(movie)
    if('Fantasy' in movie['genre']):
        fantasyMovies.append(movie)
    if('Family' in movie['genre']):
        familyMovies.append(movie)
    if('Musical' in movie['genre']):
        musicalMovies.append(movie)
    if('Thriller' in movie['genre']):
        thrillerMovies.append(movie)



def publishAction():
    print("#################### Publishing Action Movies ###################")
    for actionmovie in actionMovies:
        #print(actionmovie)
        publisher.send("action", actionMovies)
        publisher.flush()
        time.sleep(2)
    print("Action Data pushed to kafka")

def publishComedy():
    print("#################### Publishing Comedy Movies ###################")
    for comedymovie in comedyMovies:
        print(comedymovie)
        publisher.send("comedy", comedymovie)
        publisher.flush()
        time.sleep(2)
    print("Comedy Data pushed to kafka")
    
def publishCrime():
    print("#################### Publishing Crime Movies ###################")
    for crimemovie in crimeMovies:
        #print(crimemovie)
        publisher.send("crime", crimemovie)
        publisher.flush()
        time.sleep(2)
    print("Crime Data pushed to kafka")

def publishDrama():
    print("#################### Publishing Drama Movies ###################")
    for dramamovie in dramaMovies:
        #print(dramamovie)
        publisher.send("drama", dramamovie)
        publisher.flush()
        time.sleep(2)
    print("Drama Data pushed to kafka")

def publishSciFi():
    print("#################### Publishing Sci-Fi Movies ###################")
    for scifimovie in scifiMovies:
        print(scifimovie)
        publisher.send("scifi", scifiMovies)
        publisher.flush()
        time.sleep(2)
    print("Sci-Fi Data pushed to kafka")

def publishAdventure():
    print("#################### Publishing Adventure Movies ###################")
    for adventuremovie in adventureMovies:
        #print(adventuremovie)
        publisher.send("adventure", adventuremovie)
        publisher.flush()
        time.sleep(2)
    print("Adventure Data pushed to kafka")
    
def publishFantasy():
    print("#################### Publishing Fantasy Movies ###################")
    for fantasymovie in fantasyMovies:
        #print(fantasymovie)
        publisher.send("fantasy", fantasymovie)
        publisher.flush()
        time.sleep(2)
    print("Fantasy Data pushed to kafka")

def publishFamily():
    print("#################### Publishing Family Movies ###################")
    for familymovie in familyMovies:
        #print(familymovie)
        publisher.send("family", familymovie)
        publisher.flush()
        time.sleep(2)
    print("Family Data pushed to kafka")

def publishMusical():
    print("#################### Publishing Musical Movies ###################")
    for musicalmovie in musicalMovies:
        #print(musicalmovie)
        publisher.send("musical", musicalmovie)
        publisher.flush()
        time.sleep(2)
    print("Musical Data pushed to kafka")

def publishThriller():
    print("#################### Publishing Thriller Movies ###################")
    for thrillermovie in thrillerMovies:
        #print(thrillermovie)
        publisher.send("thriller", thrillermovie)
        publisher.flush()
        time.sleep(2)
    print("Thriller Data pushed to kafka")
    
if __name__ == "__main__":
    
    publishComedy()
    publishAction()
    publishSciFi()
    publishCrime()
    publishDrama()
    publishAdventure()
    publishFamily()
    publishMusical()
    publishThriller()
    publishFantasy()
