import imdb
import csv
import time

moviesDB=imdb.IMDb()

movies_list=[]
movies_info = []
#movies_dict = {}

with open('test.csv') as csvfile:
     file = csv.reader(csvfile)
     
     for row in file:
         movies_list.append(row[0])

#for i in movies_list:
#    print(i)

for j in range(0,len(movies_list)):
    movies=moviesDB.search_movie(movies_list[j],results=1)
    movies_dict = {}
  
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
    
        movies_dict['_id']=j+1
        movies_dict['genre']=genre
        movies_dict['movie_info']={'title':title,'rating':rating,'directors':str(directors),'year':year,'casting':casting}
        movies_dict['language']=language
    
    movies_info.append(movies_dict)

#for i in movies_dict:
#    print(i)

def getHindi():
     filtered_dict_hindi = [{k:v for (k,v) in i.items() if 'Hindi' in i['language']} for i in movies_info]
     filter_hindi=[x for x in filtered_dict_hindi if x]

     return filter_hindi

def getEnglish():
     filtered_dict_english = [{k:v for (k,v) in i.items() if 'English' in i['language']} for i in movies_info]
     filter_english=[x for x in filtered_dict_english if x]

     return filter_english

def getTamil():
     filtered_dict_tamil = [{k:v for (k,v) in i.items() if 'Tamil' in i['language']} for i in movies_info]
     filter_tamil=[x for x in filtered_dict_tamil if x]  

     return filter_tamil

#def getAction():
#    filtered_dict_action = [{k:v for (k,v) in i.items() if 'Action' in i['genre']} for i in movies_info]
#    filter_action=[x for x in filtered_dict_action if x]
    
#    return filter_action

# filtered_dict_action = [{k:v for (k,v) in i.items() if 'Action' in i['genre']} for i in movies_info]
# filter_action=[x for x in filtered_dict_action if x]

# for i in filter_action:
#     print(i)
#     time.sleep(4)


