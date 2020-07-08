

import requests
import json

response = requests.get('https://api.nytimes.com/svc/search/v2/articlesearch.json?q=computer%20security&page=0&api-key=UG6f30PnzgFUgFKQ1lu1H1HvGMS0GOta')
cyberdata = response.json()
documents = cyberdata['response']['docs']
cleansed_document_list = []
for doc in documents:
    cleansed_document_list.append(
        {
            'abstract': doc['abstract'],
            'web_url': doc['web_url'],
            'main': doc['headline']['main'],
            'image':'https://static01.nyt.com/' + doc['multimedia'][0]['url']
        }
        
    )
print(json.dumps(cleansed_document_list, indent=4, sort_keys=True))
# print(cyberdata)