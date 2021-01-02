from django.shortcuts import render
from django.http import HttpResponse
import requests


def home(request):
    return render(request, "home/index.html", {'title': 'home'})


def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>')
