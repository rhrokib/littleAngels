from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.contrib.auth.models import User
from django.db import models
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.shortcuts import redirect


def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    elif request.user.profile.user_type == 'null':
        return redirect('account_setup')  # needs defined as valid ur
    return render(request, "home/index.html", {'title': 'home'})


def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>')
