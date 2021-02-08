from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Article

# Create your views here.

# @login_required(login_url='login')
def home(request):
    return render(request, "circle/home.html", context={})


def article(request):
    return render(request, "circle/home.html")


def search(request):

    article = Article.objects.all()

    return render(request, "circle/result.html", context={'articles': articles})


def user(request):
    pass


def update(request):
    pass
