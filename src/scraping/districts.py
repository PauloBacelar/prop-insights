import csv

districts = {
    "zona norte": [],
    "zona sul": [],
    "zona leste": [],
    "zona oeste": [],
    "centro": [],
}

with open("utils/distritos-sp.csv", mode="r") as file:
    zones = list(districts.keys())
    zoneIndex = 0

    csvFile = csv.reader(file)
    for line in csvFile:
        zone = zones[zoneIndex]

        if len(line) > 0:
            district_name = line[0].lower().replace("vila", "vl").replace("parque", "pq").replace("jardim", "jd")
            districts[zone].append(district_name)
        else:
            zoneIndex += 1