import tmdbsimple as tmdb
import csv
import json
import os
from dotenv import load_dotenv
import random
from app import APP_ENV
from genre_codes import genre_codes

load_dotenv()

tmdb.API_KEY='c4c3cb40b87c5d67f381e5bbdc3763ca'

#Genre = os.getenv("COUNTRY_CODE", default="US")
#ZIP_CODE = os.getenv("ZIP_CODE", default="20057")

def set_movie_settings():
    if APP_ENV == "development":
        movie_genre = str(input("Select Movie Genre: "))
        vote_average = str(input("Minimum Movie Rating: "))
        movie_year = str(input("Movies Released in Year: "))
        runtime_min = str(input("Minimum Runtime: "))
        runtime_max = str(input("Maximum Runtime: "))
        movie_certification = str(input("Enter Movie Certification"))
        #movie_year_start = input("Movies Released After Year:")
    #else:
    #    user_country = COUNTRY_CODE
    #    user_zip = ZIP_CODE
    return movie_genre, vote_average, movie_year, runtime_min, runtime_max, movie_certification #movie_year_start

pick_movie_genre, pick_vote_average, pick_movie_year, pick_runtime_min, pick_runtime_max, pick_certification = set_movie_settings()
print(pick_movie_genre)
print(type(pick_movie_genre))

if bool(pick_movie_year) == True:
    movie_year = int(pick_movie_year)
else:
    movie_year = None

if bool(pick_vote_average) == True:
    vote_average = float(pick_vote_average)
else:
    vote_average = None

if bool(pick_runtime_min) == True:
    runtime_min = float(pick_runtime_min)
else:
    runtime_min = None

if bool(pick_runtime_max) == True:
    runtime_max = int(pick_runtime_max)
else:
    runtime_max = None

if bool(pick_runtime_max) == True:
    runtime_max = int(pick_runtime_max)
else:
    runtime_max = None

if bool(pick_certification) == True:
    movie_certification= str(pick_certification)
else:
    movie_certification = None

print(type(movie_year))
print(type(vote_average))

def genre_string_to_id():
    ids_list = []
    genre_select = genre_codes['genres']
    for genre in genre_select:
        if genre['name'] == pick_movie_genre:
            genre_id = str(genre['id'])
            ids_list.append(genre_id)
            break
    if not ids_list:
        genre_id = None
    return genre_id

genre_number=genre_string_to_id()
print(type(genre_number))
print(genre_number)

page_numbers = []

p = 1
while p<100:
    page_numbers.append(p)
    p = p + 1

discover = tmdb.Discover()
movie_ids = []
for page_number in page_numbers:
    response = discover.movie(sort_by="popularity.desc", with_genres=genre_number, vote_average_gte=vote_average, 
    primary_release_year=movie_year, primary_release_date_gte=None, with_runtime_gte=runtime_min, with_runtime_lte=runtime_max, 
    certification_country="US", certification=movie_certification, page=page_number)
    for value in response['results']:
        id = value['id']
        movie_ids.append(id)
    
movies_list = []

n = 0
while n<3:
    movie_choice = random.choice(movie_ids)
    movies_list.append(movie_choice)
    movie_ids.remove(movie_choice)
    n = n+1

for single_movie in movies_list:
    movie = tmdb.Movies(single_movie)
    response = movie.info()  
    title = movie.title
    plot = movie.overview
    runtime = movie.runtime
    year = movie.release_date
    score = movie.vote_average
    genres = movie.genres

    print("Movie Name: " + str(title) + '\n')
    print("Additional Information")
    print("Overview: " + str(plot))
    print("Length: " + str(runtime) + " minutes")
    print("Release Date: " + str(year))
    print("Movie Rating: " + str(score) + "/10\n")
    print("Genre(s):")
    for genre in genres:
        print(genre['name'])
    print("\n")
        

