from django.urls import reverse
from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404

from datetime import datetime
from termcolor import cprint

from .models import Article, Person, Message, Tag, Chat


import logging

# Get an instance of a logger
logger = logging.getLogger(__file__)

# Create your views here.

# @login_required(login_url='login')
def home(request):
	# logger.debug("This logs a debug message.")
	# logger.info("This logs an info message.")
	# logger.warning("This logs a warning message.")
	# logger.error("This logs an error message.")
	return render(request, "circle/home.html", context={})


def addPerson(request):

	user_id = User.objects.get(pk=request.user.id)

	try:
		bio = str(request.POST.get("bio"))
	except KeyError:
		return render(request, "circle/error.html", context={"message":  "Enter a Bio.!!", "type": "Key Error", "link": "articles"})
	except ValueError:
		return render(request, "circle/error.html", context={"message": "Invalid Value to given field.!!", "type": "Value Error", "link": "articles"})
	except TypeError:
		return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error", "link": "articles"})

	try:
		first = str(request.POST.get("first"))
	except KeyError:
		return render(request, "circle/error.html", context={"message":  "Enter a First Name.!!", "type": "Key Error", "link": "articles"})
	except ValueError:
		return render(request, "circle/error.html", context={"message": "Invalid Value to given field.!!", "type": "Value Error", "link": "articles"})
	except TypeError:
		return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error", "link": "articles"})

	try:
		last = str(request.POST.get("last"))
	except KeyError:
		return render(request, "circle/error.html", context={"message":  "Enter a Last Name.!!", "type": "Key Error", "link": "articles"})
	except ValueError:
		return render(request, "circle/error.html", context={"message": "Invalid Value to given field.!!", "type": "Value Error", "link": "articles"})
	except TypeError:
		return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error", "link": "articles"})

	try:
		age = int(request.POST.get("age"))
	except KeyError:
		return render(request, "circle/error.html", context={"message": "Enter a Age!", "type": "Key Error.!!", "link": "articles"})
	except ValueError:
		return render(request, "circle/error.html", context={"message": "Invalid Value to given field.!!", "type": "Value Error", "link": "articles"})
	except TypeError:
		return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error", "link": "articles"})

	try:
		sex = str(request.POST.get("sex"))
	except KeyError:
		return render(request, "circle/error.html", context={"message": "Select gender from the options provided.!!", "type": "KeyError", "link": "articles"})
	except ValueError:
		return render(request, "circle/error.html", context={"message": "Invalid Value to given field.!!", "type": "Value Error", "link": "articles"})
	except TypeError:
		return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error", "link": "articles"})

	sex = sex[0]

	try:
		email = str(request.POST.get("email"))
	except KeyError:
		return render(request, "circle/error.html", context={"message": "Enter an e-mail address.!!", "type": "KeyError", "link": "articles"})
	except ValueError:
		return render(request, "circle/error.html", context={"message": "Invalid Value to given field.!!", "type": "Value Error", "link": "articles"})
	except TypeError:
		return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error", "link": "articles"})

	ph_no = (9378214503 + (user_id * 10) % request.user.id)

	try:
		ph_no = str(request.POST.get("ph_no"))
	except KeyError:
		return render(request, "circle/error.html", context={"message": "Enter an e-mail address.!!", "type": "KeyError", "link": "articles"})
	except ValueError:
		return render(request, "circle/error.html", context={"message": "Invalid Value to given field.!!", "type": "Value Error", "link": "articles"})
	except TypeError:
		return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error", "link": "articles"})

	username = email.split('@')[0]

	# person = 
	Person.objects.create(username=username, bio=bio, first=first, last=last, age=age, sex=sex, email=email, ph_no=ph_no)
	# person.save()

	return HttpResponseRedirect(reverse("person", args=(user_id, )))


def person(request, person_id):
	person = Person.object.get(id=person_id)
	return render(request, "circle/person.html", context={"person": person})


def persons(request):
	persons = Person.object.all().order_by(id)
	return render(request, "circle/persons.html", context={"persons": persons})


def newArticle(request):
	return render(request, "circle/newArticle.html", context={})

	
def addArticle(request):
	try:
		title = str(request.POST.get("title"))
	except KeyError:
		return render(request, "circle/error.html", context={"message": "Enter title.!!", "type": "Key Error", "link": "articles"})
	except ValueError:
		return render(request, "circle/error.html", context={"message": "Invalid Value to given field.!!", "type": "Value Error", "link": "articles"})
	except TypeError:
		return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error", "link": "articles"})

	try:
		description =  str(request.POST.get('description'))
	except KeyError:
		return render(request, "circle/error.html", context={"message": "Enter title.!!", "type": "Key Error", "link": "articles"})
	except ValueError:
		return render(request, "circle/error.html", context={"message": "Invalid Value to given field.!!", "type": "Value Error", "link": "articles"})
	except TypeError:
		return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error", "link": "articles"})

	
	try:
		image = str(request.POST.get('image'))
	except KeyError:
		return render(request, "circle/error.html", context={"message": "Enter title.!!", "type": "Key Error", "link": "articles"})
	except ValueError:
		return render(request, "circle/error.html", context={"message": "Invalid Value to given field.!!", "type": "Value Error", "link": "articles"})
	except TypeError:
		return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error", "link": "articles"})


	try:
		price = float(request.POST.get('price'))
	except KeyError:
		return render(request, "circle/error.html", context={"message": "Enter title.!!", "type": "Key Error", "link": "articles"})
	except ValueError:
		return render(request, "circle/error.html", context={"message": "Invalid Value to given field.!!", "type": "Value Error", "link": "articles"})
	except TypeError:
		return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error", "link": "articles"})


	try:
		tags = list(request.POST.get('tags'))
	except KeyError:
		return render(request, "circle/error.html", context={"message": "Enter title.!!", "type": "Key Error", "link": "articles"})
	except ValueError:
		return render(request, "circle/error.html", context={"message": "Invalid Value to given field.!!", "type": "Value Error", "link": "articles"})
	except TypeError:
		return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error", "link": "articles"})

	article = Article(title=title, description=description, image=image, price=price, tags=tags)

	article.save()

	return render(request, "circle/home.html", context={})


def article(request, article_id):
	article = Article.objects.get(pk=article_id)
	return render(request, "circle/article.html", context={"article": article})


def articles(request):
	articles = Article.objects.all()
	return render(request, "circle/articles.html", context={"articles": articles})


def search(request):
	return render(request, "circle/search.html", context={})


def result(request):
	try:
		search = str(request.POST.get("search"))
	except KeyError:
		return render(request, "circle/error.html", context={"message":  "Enter a Bio.!!", "type": "Key Error", "link": "articles"})
	except ValueError:
		return render(request, "circle/error.html", context={"message": "Invalid Value to given field.!!", "type": "Value Error", "link": "articles"})
	except TypeError:
		return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error", "link": "articles"})

	print()
	cprint(search, 'white')

	if len(search) == 0:
		logger.error('Search went wrong.!')

	articles = Article.objects.filter(Q(title__contains=search) | Q(description__contains=search))

	cprint(articles.query, 'magenta')
	print()

	return render(request, "circle/result.html", context={'articles': articles})


def user(request):
    return render(request, "circle/user.html", context={})


def users(request):
    return render(request, "circle/users.html", context={})

def rent(request, article_id):

	user_id = request.user.id

	article = Article.objects.get(pk=article_id)

	person = Person.objects.get(user_id=user_id)

	if article in person.bought:
		return HttpResponse('Already Bought.!')

	if article in person.cart:
		return HttpResponse('Already in Cart.!')

	if article in person.rented:
		return HttpResponse('Already Rented.!')

def wishlist(request):
	pass

def cart(request):

	person_id = 1
	person = Person.objects.get(pk=person_id)
	articles = person.cart
	return render(request, "circle/cart.html", context={"articles": articles})


def chat(request, chat_id):
	chat = Chat.objects.get(pk=chat_id)
	return render(request, "circle/chat.html", context={"chat": chat})


def chats(request):
	chats = Chat.objects.all()
	return render(request, "circle/chats.html", context={"chats": chats})


def update(request):
    return render(request, "circle/user.html", context={})


def message(request, sender_id, receiver_id):


	try:
		chat_id = float(request.POST.get('chat_id'))
	except KeyError:
		return render(request, "circle/error.html", context={"message": "Enter title.!!", "type": "Key Error", "link": "articles"})
	except ValueError:
		return render(request, "circle/error.html", context={"message": "Invalid Value to given field.!!", "type": "Value Error", "link": "articles"})
	except TypeError:
		return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error", "link": "articles"})


	try:
		text = list(request.POST.get('text'))
	except KeyError:
		return render(request, "circle/error.html", context={"message": "Enter text.!!", "type": "Key Error", "link": "articles"})
	except ValueError:
		return render(request, "circle/error.html", context={"message": "Invalid Value to given field.!!", "type": "Value Error", "link": "articles"})
	except TypeError:
		return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error", "link": "articles"})

	message = Message.objects.create(text=text, timestamp=datetime.now())

	chat = Chat.objects.get(pk=chat_id)
	chat.messages.add(message)

	chat.save()

	return HttpResponseRedirect(reverse("chat", args=(chat_id, )))


def login(request):
    return render(request, "circle/home.html", context={})


def logout(request):
    return render(request, "circle/home.html", context={})


def error(request):
	return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error", "link": "articles"})
