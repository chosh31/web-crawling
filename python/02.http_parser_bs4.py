from urllib import request, parse
from bs4 import BeautifulSoup
from elasticsearch import Elasticsearch

es = Elasticsearch()
rss = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'

values = { 'stnId' : '108' }
params = parse.urlencode(values)

url = rss + '?' + params

print('url=', url)

data = request.urlopen(url).read()
text = data.decode('utf-8')

bs = BeautifulSoup(text, 'html.parser')

locations = bs.find_all("location") 

print("-------------------------")
for location in locations:
    
    city = location.find('city')
    print(city.text)
    for data in location.find_all('data'):
        tmef = data.find("tmef").text
        wf = data.find('wf').text
        tmn = data.find('tmn').text
        tmx = data.find('tmx').text
        reliability = data.find('reliability').text
        print('{0} ({1}~{2}) - {3}'.format(tmef, tmn, tmx, wf)) 
    print("-------------------------")