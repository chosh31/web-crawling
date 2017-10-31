import urllib.request

url = "http://localhost:9200"
res = urllib.request.urlopen(url)
data = res.read()

text = data.decode('utf-8')
print(text)