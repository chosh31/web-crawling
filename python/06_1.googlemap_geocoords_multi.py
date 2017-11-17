import json
import requests

addrs = ['sadang', 'tokyo', 'busan'];
key = '';

for addr in addrs:
	r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' + addr + '&key=' + key);
	# print(r.text);
	jsonObj = json.loads(r.text)
	# print(jsonObj);

	results = jsonObj['results']
	for result in results:
		print(addr);
		print(result['geometry']['location'])