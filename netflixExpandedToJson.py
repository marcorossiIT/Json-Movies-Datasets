import json
import csv

movieList = []
with open(file="originals/Netflix Dataset Latest 2021.tsv", mode="rt") as file:
    tsvFile = csv.reader(file, delimiter="\t")
    movieTable = list(tsvFile)
    headers = tuple(movieTable[0][:-2])
    movies = movieTable[1:]
    for movie in movies:
        movieProperties = dict()
        i_property = 0
        for header in headers:
            if header == "Genre" or header == "Tags" or header == "Languages" or header == "Country Availability" or header == "Director" or header == "Writer" or header == "Actors" or header == "Production House" :
                movieProperties[header] = movie[i_property].split(",")
            else:
                movieProperties[header] = movie[i_property]

            i_property += 1
        movieList.append(movieProperties)

with open(file="generated/netflixExpandedDataset.json", mode="w") as file:  
    file.write(json.dumps(movieList))
        
    