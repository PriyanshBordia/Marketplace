from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404

from .models import Article

# Create your views here.

# @login_required(login_url='login')
def home(request):
    return render(request, "circle/home.html", context={})


def article(request):
    return render(request, "circle/user.html")


def search(request):
    return render(request, "circle/search.html", context={})


def result(request):

    articles = Article.objects.all()
    return render(request, "circle/result.html", context={'articles': articles})


def user(request):
    return render(request, "circle/user.html", context={})


def update(request):
    return render(request, "circle/user.html", context={})
