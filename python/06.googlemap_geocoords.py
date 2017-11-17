import json
import requests

addr = 'sadang';
key = '';
r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' + addr + '&key=' + key);
jsonObj = json.loads(r.text)

# print(jsonObj);

results = jsonObj['results']
for result in results:
    print(result['geometry']['location'])