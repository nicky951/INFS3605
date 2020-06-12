from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.


def index(request):
    return HttpResponse("Page 2")

def testhtml(request):
    return render(request, 'webapp/index.html')
