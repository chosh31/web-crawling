from urllib import request, parse
from bs4 import BeautifulSoup
from datetime import datetime
from elasticsearch import Elasticsearch

rss = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'

values = { 'stnId' : '108' }
params = parse.urlencode(values)

url = rss + '?' + params

print('url=', url)

data = request.urlopen(url).read()
text = data.decode('utf-8')

bs = BeautifulSoup(text, 'html.parser')

locations = bs.find_all("location") 

es = Elasticsearch()
for location in locations:    
    city = location.find('city').text    
    for data in location.find_all('data'):
        date = data.find("tmef").text
        forecast = data.find('wf').text
        tmin = data.find('tmn').text
        tmax = data.find('tmx').text  
        
        body = {
            "city": city,
            "date": date,
            "forecast": forecast,
            "tmin": tmin,
            "tmax": tmax
        }

        es.index(index="weather_2017", doc_type="record", body=body)