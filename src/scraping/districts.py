import csv

def to_kebab_case(string):
    return '-'.join(string.split(' '))

def abbreviate_string(string):
    return string.replace("vila", "vl").replace("parque", "pq").replace("jardim", "jd")


districts_list = {
    "zona-norte": [],
    "zona-sul": [],
    "zona-leste": [],
    "zona-oeste": [],
    "centro": [],
}

with open("utils/distritos-sp.csv", mode="r") as file:
    zones = list(districts_list.keys())
    zoneIndex = 0

    csvFile = csv.reader(file)
    for line in csvFile:
        zone = zones[zoneIndex]

        if len(line) > 0:
            district_name = to_kebab_case(abbreviate_string(line[0].lower()))
            districts_list[zone].append(district_name)
        else:
            zoneIndex += 1
