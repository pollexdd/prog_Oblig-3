# fikk litt hjelp her: https://pythonexamples.org/python-list-of-dictionaries/


from traceback import print_tb


liste = [
{
    "name":"Con air",
    "year": 1997,
    "rating": 6.9 
}
,
{
    "name":"Inside out",
    "year": 2015,
    "rating": 8.1 
},
{
    "name": "Inception",
    "year": 2010,
    "rating": 8.7 
}
]


    

def addMovie(list_of_movies, name, year, rating=5.0):
    list_of_movies.append({"name": name ,"year": year, "rating": rating})


addMovie(liste, "shrek", 2001, 7.1)
addMovie(liste, "Money ball", 2011, 7.6)
addMovie(liste, "Happy Gilmore", 1996, 7.0)
addMovie(liste, "National Treasure", 2004, )


print(liste)

def filmerPrint(liste_of_movies):
    for movie in liste_of_movies:
        print(f" {movie['name']} - {movie['year']} has a rating of {movie['rating']} ")
     
filmerPrint(liste)  


def gjennomsnitt(liste_of_movies):
    nummer= 0
    for movie in liste_of_movies:
        nummer = nummer +  movie["rating"]
        avg = nummer / len(liste_of_movies)
    print(avg)

gjennomsnitt(liste)

liste_2 = []
def yearOfMovies(liste_of_movies):
    for movie in liste_of_movies:
        if movie["year"] <= 2010:
            liste_2.append(movie)
            print(liste_2)

yearOfMovies(liste)
