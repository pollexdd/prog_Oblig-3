# fikk litt hjelp her: https://pythonexamples.org/python-list-of-dictionaries/


from ast import Num


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
    }
    ,
    {
        "name": "Inception",
        "year": 2010,
        "rating": 8.7 
    }
    ]





for keys in liste:

   


    # def funk(list):
     liste.append({"name": input("navn på film 1 " ), "year" : input("år på film 1 "), "rating" : None})
    #     # liste.append({"name": input("navn på film 2 " ), "year" : input("år på film 2 "), "rating" : input("rating på film 2" )})
    #     # liste.append({"name": input("navn på film 3 " ), "year" : input("år på film 3 "), "rating" : input("rating på film 3 ")})
    #     # liste.append({"name": input("navn på film 4 " ), "year" : input("år på film 4 "), "rating" : input("rating på film 4 ")})
    #     # liste.append({"name": input("navn på film 5 " ), "year" : input("år på film 5 "), "rating" : input("rating på film 5 ")})



        
            
    # funk(list)
    # print(list)


    def funk_print(liste):
        print(liste[0]["name"],"-",liste[0]["year"],"has a rating of", liste[0]["rating"])
        print(liste[1]["name"],"-",liste[1]["year"],"has a rating of", liste[1]["rating"])
        print(liste[2]["name"],"-",liste[2]["year"],"has a rating of", liste[2]["rating"])


    funk_print(liste)


    def funk_gjennom(liste):
    funk_gjennom(liste)