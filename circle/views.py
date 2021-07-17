import random
from django.urls import reverse
from django.db.models import Q
from django.shortcuts import redirect, render
# from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, Http404

from datetime import datetime
from termcolor import cprint

from .models import Article, Person, Message, Tag, Chat
from .forms import ArticleForm, PersonForm, TagForm

# import logging

# Get an instance of a logger
# logger = logging.getLogger(__file__)

# Create your views here.

def home(request):
	# logger.debug("This logs a debug message.")
	# logger.info("This logs an info message.")
	# logger.warning("This logs a warning message.")
	# logger.error("This logs an error message.")
	return render(request, "circle/home.html", context={})


def newPerson(request):
	form = PersonForm()
	return render(request, "circle/newPerson.html", context={"form": form})

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
	Person.objects.create(user=user_id, username=username, bio=bio, first=first, last=last, age=age, sex=sex, email=email, ph_no=ph_no)
	# person.save()

	return HttpResponseRedirect(reverse("person", args=(user_id, )))


def person(request, slug):
	
	user_id = request.user.id
	
	user = User.objects.get(pk=user_id)

	person = Person.objects.filter(user=user, slug=slug).first()
	
	# cprint(person.bookmarked, 'magenta')
	# if person is None:
		# cprint("yes", 'red')
	# cprint(person.query, 'white')
	# person.first()
	return render(request, "circle/person.html", context={"person": person})


def persons(request):
	persons = Person.objects.all().order_by('id')
	# cprint(persons.query, 'magenta')
	return render(request, "circle/persons.html", context={"persons": persons})


def newArticle(request):
	form = ArticleForm()
	return render(request, "circle/newArticle.html", context={"form": form})

	
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

	articles = Article.objects.filter(Q(title__contains=search) | Q(description__contains=search))

	cprint(articles.query, 'magenta')
	print()

	return render(request, "circle/result.html", context={'articles': articles})


def rented(request, article_id):

	user_id = request.user.id

	article = Article.objects.get(pk=article_id)

	person = Person.objects.get(user_id=user_id)

	if article in person.bought:
		return HttpResponse('Already Bought.!')

	if article in person.cart:
		return HttpResponse('Already in Cart.!')

	if article in person.rented:
		return HttpResponse('Already Rented.!')


def rent(request, article_id):
	user_id = request.user.id

	person = Person.objects.filter(user=user_id).first()

	article = Article.objects.get(pk=article_id)

	if person is not None and article is not None:
		if article not in person.rented.all():
			person.rented.add(article)	
			person.save()
			return HttpResponse('Article Added.!')
		else:
			return HttpResponse('Already Present.!')

	return HttpResponseRedirect(reverse("article", args=(article_id, )))


def bookmark(request, article_id):
	user_id = request.user.id

	person = Person.objects.filter(user=user_id).first()
	cprint(person, 'white')
	article = Article.objects.get(pk=article_id)
	cprint(article, 'red')

	if person is not None and article is not None:
		person.bookmarked.add(article)
		person.save()

	return HttpResponseRedirect(reverse("article", args=(article_id, )))


def buy(request, article_id):
	user_id = request.user.id

	person = Person.objects.filter(user=user_id).first()

	article = Article.objects.get(pk=article_id)

	if person is not None and article is not None:
		if article not in person.carted.all():
			person.carted.add(article)
			person.save()
			return HttpResponse()
		else:
			return HttpResponse('Already Present.!')

	return HttpResponseRedirect(reverse("article", args=(article_id, )))


def wishlist(request):
	user_id = request.user.id

	person = Person.objects.filter(user=user_id).first()
	
	cprint(person, 'blue')

	if person is not None:
		articles = person.bookmarked.all
		return render(request, "circle/wishlist.html", context={"articles": articles})
	else:
		return render(request, "circle/error.html", context={"message": "No person registered.!!", "type": "Data Error!!", })


def cart(request):
	user_id = request.user.id

	person = Person.objects.get(user=user_id).first()
	
	if person is not None:
		articles = person.carted.all()

	return render(request, "circle/cart.html", context={"articles": articles})


def chat(request, chat_id):
	chat = Chat.objects.get(pk=chat_id)
	return render(request, "circle/chat.html", context={"chat": chat})


def chats(request):
	# person_id = 1
	chats = Chat.objects.all()
	cprint(chats, 'white')
	return render(request, "circle/chats.html", context={"chats": chats})


def update(request):
	user_id = request.user.id

	try:
		first = str(request.POST.get("first"))
	except KeyError:
		return render(request, "flights/error.html", context={"message":  "Enter a First Name!!", "type": "Key Error!!"})
	except ValueError:
		return render(request, "flights/error.html", context={"message": "Invalid Value to given field!!", "type": "Value Error!!"})
	except TypeError:
		return render(request, "flights/error.html", context={"message": "Incompatible DataType!!", "type": "Type Error!!", })

	try:
		last = str(request.POST.get("last"))
	except KeyError:
		return render(request, "flights/error.html", context={"message":  "Enter a Last Name!!", "type": "Key Error!!"})
	except ValueError:
		return render(request, "flights/error.html", context={"message": "Invalid Value to given field!!", "type": "Value Error!!"})
	except TypeError:
		return render(request, "flights/error.html", context={"message": "Incompatible DataType!!", "type": "Type Error!!", })

	try:
		email = str(request.POST.get("email"))
	except KeyError:
		return render(request, "flights/error.html", context={"message": "Enter a e-mail address!!", "type": "KeyError!!"})
	except ValueError:
		return render(request, "flights/error.html", context={"message": "Invalid Value to given field!!", "type": "Value Error!!"})
	except TypeError:
		return render(request, "flights/error.html", context={"message": "Incompatible DataType!!", "type": "Type Error!!", })

	user = User.objects.get(pk=user_id)

	user.first_name = first
	user.last_name = last
	user.email = email
	user.save()

	try:
		user = User.objects.get(pk=user_id)
	except user.DoesNotExist:
		return render(request, "flights/error.html", context={"message": "User Doesn't Exist!", "type": "Value DoesNotExist.!!", })

	return render(request, "circle/user.html", context={"user": user})


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


def error(request):
	return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error", "link": "articles"})


def user(request, user_id):
	user = User.objects.get(pk=user_id)
	return render(request, "circle/user.html", context={"user": user})


def users(request):
	users = User.objects.all()
	return render(request, "circle/users.html", context={"users": users})


def friends(request):
    return render(request, "circle/friends.html", context={})


"""

import http.client

def verification(request):

	ph_no = 9316300064
	request.session['ph_no'] = ph_no

	otp = str(random.randint(100000, 999999))

	cprint(otp, 'white')

	connection = http.client.HTTPSConnection("api.msg91.com")

	authkey = settings.authkey

	code = 91
	sender = "Marketplace Team"
	# payload = "{\"Value1\":\"Param1\",\"Value2\":\"Param2\",\"Value3\":\"Param3\"}"

	headers = {'content-type': "application/json"}

	connection.request("GET", "http://control.msg91.com/api/sendotp.php", params = {"otp": otp, "mobile": ph_no, "sender": sender, "message": message, "country": code, "authkey": authkey, "otp_length": 6}, headers=headers)

	res = connection.getresponse()
	data = res.read()

	print(data)

	print(data.decode("utf-8"))

	return render(request, "circle/test.html", context={"message": "OTP sent.!!"})


"""
