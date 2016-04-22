import json
from pprint import pprint


json_data = open("./some.json")
data = json.load(json_data)

for d in data:
    print(str(d["pagetitle"]))
    print(d["pagetitle"].encode('utf-8'))
