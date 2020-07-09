from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests
import json

# Create your views here.
# UG6f30PnzgFUgFKQ1lu1H1HvGMS0GOta
# https://api.nytimes.com/svc/search/v2/articlesearch.json?q=computer%20security&page=0&api-key=UG6f30PnzgFUgFKQ1lu1H1HvGMS0GOta


#Haveibeenpwned https://haveibeenpwned.com/unifiedsearch/nicholasliang325%40gmail.com
def home(request):
    template = loader.get_template('home.html')
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
    context = {
        'cleansed_document_list': cleansed_document_list,
    }
    return HttpResponse(template.render(context, request))

#if this returns an no response, no breaches
def pwned(request):
    template = loader.get_template('pwned.html')

    headers = {
        "hibp-api-key": "38eb580ec92d4403becca47370ac9d1f"
    }

    response = requests.get('https://haveibeenpwned.com/api/v3/breachedaccount/nicholasliang325@gmail.com?truncateResponse=false', headers=headers)

    breachdata = response.json()

    cleansedbreach = []
    for compromised in breachdata:
        cleansedbreach.append(
            {
                'Name':compromised['Name'],
                'BreachDate':compromised['BreachDate'],
                'LogoPath':compromised['LogoPath'],
                'Description':compromised['Description']
            }
        )
    context = {'cleansedbreach':cleansedbreach}
    return HttpResponse(template.render(context, request))