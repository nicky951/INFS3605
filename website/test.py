

import json
import requests
response = requests.get('https://api.nytimes.com/svc/search/v2/articlesearch.json?q=computer%20security&page=0&api-key=9B7vbP7Jp0KdeksqwGgAQkemvyQZRHgP')
cyberdata = response.json()
documents = cyberdata['response']['docs']
cleansed_document_list = []
for doc in documents:
    print(len(doc['multimedia']))