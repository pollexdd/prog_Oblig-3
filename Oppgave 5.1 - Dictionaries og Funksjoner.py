# fikk litt hjelp her: https://pythonexamples.org/python-list-of-dictionaries/

list = [
{
    "name":"Con air",
    "year": "1997",
    "rating": "69" 
}
,
{
    "name":"Inside out",
    "year": "2015",
    "rating": "8.1" 
},
{
    "name": "Inception",
    "year": "2010",
    "rating": "8.7" 
}
]

def funk(list):
    list.append({"name":"Bee Movie", "year" : "2007", "rating" : "6.1"})
    list.append({"name":"Money ball", "year" : "2011", "rating" : "7.6"})
    list.append({"name":"The wolf of wallstreet", "year" : "2013", "rating" : "8.2"})
    list.append({"name":"Shrek", "year" : "2001", "rating" : "7.9"})

funk(list)
print(list)