import json
import requests

r = requests.get('http://localhost:9200/weather_2017/_search')
json = json.loads(r.text)

hits = json['hits']['hits']
for hit in hits:
    print(hit['_source'])