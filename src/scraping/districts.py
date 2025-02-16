import csv

def to_kebab_case(string):
    return '-'.join(string.split())


def abbreviate_string(string):
    abbreviations = {"vila": "vl", "parque": "pq", "jardim": "jd"}
    for word, abbr in abbreviations.items():
        string = string.replace(word, abbr)
    return string


districts_list = {
    "zona-norte": [],
    "zona-sul": [],
    "zona-leste": [],
    "zona-oeste": [],
    "centro": [],
}

with open("utils/distritos-sp.csv", mode="r", encoding="utf-8") as file:
    csv_reader = csv.reader(file)
    zones = iter(districts_list.keys())
    current_zone = next(zones, None)

    for line in csv_reader:
        if line:
            district_name = to_kebab_case(abbreviate_string(line[0].lower()))
            districts_list[current_zone].append(district_name)
        else:
            current_zone = next(zones, None)
