from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    html = "<h1> Log In</h1><br><h2>Sign Up</h2>"
    return HttpResponse(html)

