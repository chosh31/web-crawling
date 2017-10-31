from urllib import request, parse
from bs4 import BeautifulSoup

url = 'http://www.hanbit.co.kr/myhanbit/myhanbit.html'

data = request.urlopen(url).read()
page = data.decode('utf-8')
print(page)