from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch()

data = "hello_world"
my_body = { "any" : data,
 "timestamp": datetime.now() 
}
es.index(index="my-index", doc_type="test-type", id=44, body=my_body)
result = es.get(index="my-index", doc_type="test-type", id=44)['_source']

print(result)