from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests
import json

# Create your views here.
# UG6f30PnzgFUgFKQ1lu1H1HvGMS0GOta
# https://api.nytimes.com/svc/search/v2/articlesearch.json?q=computer%20security&page=0&api-key=UG6f30PnzgFUgFKQ1lu1H1HvGMS0GOta

def home(request):
    template = loader.get_template('home.html')
    response = requests.get('https://api.nytimes.com/svc/search/v2/articlesearch.json?q=computer%20security&page=0&api-key=9B7vbP7Jp0KdeksqwGgAQkemvyQZRHgP')
    cyberdata = response.json()
    documents = cyberdata['response']['docs']
    cleansed_document_list = []
    for doc in documents:
        if len(doc['multimedia']) > 0:
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

    # headers = {
    #     "hibp-api-key": "38eb580ec92d4403becca47370ac9d1f"
    # }

    # response = requests.get('https://haveibeenpwned.com/api/v3/breachedaccount/nicholasliang325@gmail.com?truncateResponse=false', headers=headers)
    
    # breachdata = response.json()

    # cleansedbreach = []
    # for compromised in breachdata:
    #     cleansedbreach.append(
    #         {
    #             'Name':compromised['Name'],
    #             'BreachDate':compromised['BreachDate'],
    #             'LogoPath':compromised['LogoPath'],
    #             'Description':compromised['Description']
    #         }
    #     )
    context = {}
    return HttpResponse(template.render(context, request))

def info(request):
    template = loader.get_template('sec_info_home.html')
    context = {}
    return HttpResponse(template.render(context, request))

def passwordpage(request):
    template = loader.get_template('passwordpage.html')
    context = {}
    return HttpResponse(template.render(context, request))

def wfhpage(request):
    template = loader.get_template('wfhpage.html')
    context = {}
    return HttpResponse(template.render(context, request))

def attackpage(request):
    template = loader.get_template('attackpage.html')
    context = {}
    return HttpResponse(template.render(context, request))

def preventionpage(request):
    template = loader.get_template('preventionpage.html')
    context = {}
    return HttpResponse(template.render(context, request))

def securitypage(request):
    template = loader.get_template('securitypage.html')
    context = {}
    return HttpResponse(template.render(context, request))

def detectionpage(request):
    template = loader.get_template('detectionpage.html')
    context = {}
    return HttpResponse(template.render(context, request))

def netsecuritypage(request):
    template = loader.get_template('netsecuritypage.html')
    context = {}
    return HttpResponse(template.render(context, request))

def policypage(request):
    template = loader.get_template('policypage.html')
    context = {}
    return HttpResponse(template.render(context, request))

def aboutuspage(request):
    template = loader.get_template('aboutuspage.html')
    context = {}
    return HttpResponse(template.render(context, request))