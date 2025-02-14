import csv

districts = {
    "norte": [],
    "sul": [],
    "leste": [],
    "oeste": [],
    "centro": [],
}


with open("utils/distritos-sp.csv", mode="r") as file:
    zones = list(districts.keys())
    zoneIndex = 0
    csvFile = csv.reader(file)
    for line in csvFile:
        if len(line) > 0:
            print(line[0].lower() + " - " + zones[zoneIndex])
        else:
            zoneIndex += 1