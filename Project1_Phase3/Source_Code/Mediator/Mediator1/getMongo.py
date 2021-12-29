import pymongo
from pymongo import MongoClient
import certifi
from pymongo.message import update
import json

ca = certifi.where()

cluster = pymongo.MongoClient("mongodb+srv://rishi:rishi@cluster0.sn3xi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",tlsCAFile=ca)

def getMovies():
    #action_movies.drop()
    #comedy_movies.drop()
    #crime_movies.drop()
    #drama_movies.drop()
    #cluster.drop_database("Movies")
    db = cluster["Movies"]
    #cluster.drop_database('Movies')
    action_movies = db["Action"]
    comedy_movies = db["Comedy"]
    crime_movies = db["Crime"]
    drama_movies = db["Drama"]
    subs=db["Subs"]


    results_action = action_movies.find({})
    list_action=[]
    list_genre_action=[]

    for result in results_action:
        list_action.append(result)
        list_genre_action.append(result['genre'])

    #print(type(db.action_movies.find_one()))
    
    results_drama = drama_movies.find({})
    list_drama=[]
    list_genre_drama=[]

    for result in results_drama:
        list_drama.append(result)
        list_genre_drama.append(result['genre'])
    
    

    results = subs.find({})
    list_subs=[]
    for result in results:
        list_subs.append(result['topic'])

    matching_dict=[]

    for i in list_subs:
        for j in range(0,len(list_genre_action)):
            if(i in list_genre_action[j]):

                matching_dict.append(list_action[j]['movie_info'])

    
    for i in list_subs:
        for j in range(0,len(list_genre_drama)):
            if(i in list_genre_drama[j]):

                matching_dict.append(list_drama[j]['movie_info'])

    final_list=[]
    for i in matching_dict:
        if i not in final_list:
            final_list.append(i)

    #print(len(matching_dict))
    #print(len(final_list))

    #print(final_list)

    jsonStr = json.dumps(final_list)

    return jsonStr




