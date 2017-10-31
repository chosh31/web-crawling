import urllib.request
import urllib.parse

rss = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'

values = { 'stnId' : '108' }
params = urllib.parse.urlencode(values)

url = rss + '?' + params

print('url=', url)

data = urllib.request.urlopen(url).read()
text = data.decode('utf-8')

print(text)