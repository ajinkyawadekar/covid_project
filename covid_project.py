import requests
import json
import ijson

url = "https://api.covid19api.com/summary"

r = requests.get(url)
pretty_json = json.loads(r.text)
file1 = (json.dumps(pretty_json, indent=2))

#covid_summary = open('covid_summary.json', 'w')
#covid_summary.writelines(file1)

filename = "covid_summary.json"
with open(filename, 'r') as f:
    objects = ijson.items(f, 'Countries.item')
    columns = list(objects)

#print(columns[0])
