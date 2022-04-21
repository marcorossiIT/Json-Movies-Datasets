import json
import csv

movieList = []
with open(file="originals/disney_plus_titles.csv", mode="rt") as file:
    tsvFile = csv.reader(file, delimiter=",")
    movieTable = list(tsvFile)
    headers = tuple(movieTable[0])
    movies = movieTable[1:]
    for movie in movies:
        movieProperties = dict()
        i_property = 0
        for header in headers:
            if header == "cast" or header == "listed_in" or header == "director" or header == "country":
                movieProperties[header] = movie[i_property].split(",")
            else:
                movieProperties[header] = movie[i_property]
            i_property += 1
        movieList.append(movieProperties)

with open(file="generated/disneyDataset.json", mode="w") as file:  
    file.write(json.dumps(movieList))
        
    