movies = [    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},   
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},    
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},    
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},    
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},    
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},    
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},    
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]
def imdb_55(movie):
    return movie["imdb"] > 5.5

def list_of_imdb_above_55(movies): 
    imdbabove55 = []
    for movie in movies:
        if(movie["imdb"] > 5.5):
            imdbabove55.append(movie)   
    return imdbabove55

def filtered_of_category(movies, category):
    category_movies = []
    for movie in movies:
        if(movie["category"].lower() == category.lower()):
            category_movies.append(movie)
    return category_movies

def average_imdb_score(movies):    
    total_imdb = 0  
    for movie in movies:
        total_imdb += movie["imdb"]

    return total_imdb / len(movies)

def compute_average_category(movies, category):    
    category_movies = filtered_of_category(movies, category)
    return average_imdb_score(category_movies)

print(imdb_55(movies[0]))
print(list_of_imdb_above_55(movies))
print(filtered_of_category(movies, "Suspense"))
print(average_imdb_score(movies))
print(compute_average_category(movies, "Romance"))