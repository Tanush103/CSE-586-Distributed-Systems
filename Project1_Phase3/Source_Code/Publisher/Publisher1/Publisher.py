import imdb
import csv
import pymongo
from pymongo import MongoClient
import certifi
from pymongo.message import update

moviesDB=imdb.IMDb()


ca = certifi.where()

cluster = pymongo.MongoClient("mongodb+srv://rishi:rishi@cluster0.sn3xi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",tlsCAFile=ca)

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




movies_list=[]
with open('test.csv') as csvfile:
     file = csv.reader(csvfile)
     
     for row in file:
         movies_list.append(row[0])


movies_info=[]

for j in range(0,len(movies_list)):
  movie_dict={}
  movies=moviesDB.search_movie(movies_list[j],results=1)
  for i in range(0,len(list(movies))):
    id=movies[i].getID()
    movie = moviesDB.get_movie(id)

    title = movie['title']
    year = movie['year'] 
    rating = movie['rating']
    directors = movie['directors'][-1]
    casting=[]
    for k in movie['cast']:
      casting.append(k['name'])
    language=[]
    for l in movie['language']:
      language.append(l)

    genre=[]
    for m in movie['genre']:
      genre.append(m)
    movie_dict['_id']=j+1
    movie_dict['genre']=genre
    movie_dict['movie_info']={'title':title,'rating':rating,'directors':str(directors),'year':year,'casting':casting}
    movie_dict['language']=language
  movies_info.append(movie_dict)

filter=[]


filtered_dict_hindi = [{k:v for (k,v) in i.items() if 'Hindi' in i['language']} for i in movies_info]
filter_hindi=[x for x in filtered_dict_hindi if x]


#filtered_dict_english = [{k:v for (k,v) in i.items() if 'English' in i['language']} for i in movies_info]
 # #new_dict.update(filtered_dict)
#filter=[x for x in filtered_dict_hindi if x]



filtered_dict_comedy = [{k:v for (k,v) in i.items() if 'Comedy' in i['genre']} for i in filter_hindi]
  #new_dict.update(filtered_dict)
filter_comedy=[x for x in filtered_dict_comedy if x]


filtered_dict_drama = [{k:v for (k,v) in i.items() if 'Drama' in i['genre']} for i in filter_hindi]
  #new_dict.update(filtered_dict)
filter_drama=[x for x in filtered_dict_drama if x]


filtered_dict_crime = [{k:v for (k,v) in i.items() if 'Crime' in i['genre']} for i in filter_hindi]
  #new_dict.update(filtered_dict)
filter_crime=[x for x in filtered_dict_crime if x]


filtered_dict_action = [{k:v for (k,v) in i.items() if 'Action' in i['genre']} for i in filter_hindi]
  #new_dict.update(filtered_dict)
filter_action=[x for x in filtered_dict_action if x]


for i in filter_action:
    action_movies.insert_one(i)

for i in filter_comedy:
    comedy_movies.insert_one(i)

for i in filter_crime:
    crime_movies.insert_one(i)

for i in filter_drama:
    drama_movies.insert_one(i)






#post_count = collection.count_documents({})
#print(post_count)





#print(filter)