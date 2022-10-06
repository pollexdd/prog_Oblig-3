# fikk litt hjelp her: https://pythonexamples.org/python-list-of-dictionaries/

liste = [
{
    "name":"Con air",
    "year": 1997,
    "rating": 69 
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


    

def funk(liste):
    liste.append({"name": input("navn på film 1 " ), "year" : input("år på film 1 "), "rating" : input("rating film1")})
    # liste.append({"name": input("navn på film 2 " ), "year" : input("år på film 2 "), "rating" : input("rating på film 2" )})
    # liste.append({"name": input("navn på film 3 " ), "year" : input("år på film 3 "), "rating" : input("rating på film 3 ")})
    # liste.append({"name": input("navn på film 4 " ), "year" : input("år på film 4 "), "rating" : input("rating på film 4 ")})
    # liste.append({"name": input("navn på film 5 " ), "year" : input("år på film 5 "), "rating" : input("rating på film 5 ")})
    

for rating in liste:
    if rating == "":
        liste[3]["rating"].append("5")


        
   
funk(liste)    
        

print(liste)