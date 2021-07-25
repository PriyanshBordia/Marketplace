import os
from django.urls import reverse
from django.db.models import Q
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404

from .utils import *

from datetime import datetime
from termcolor import cprint

from .models import Article, Person, Message, Tag, Chat
from .forms import ArticleForm, PersonForm, TagForm, MessageForm

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


@login_required
def newPerson(request):
	form = PersonForm()
	tags = Tag.objects.all()
	return render(request, "circle/newPerson.html", context={"form": form, "tags": tags})


@login_required
def addPerson(request):
	if request.GET:
		return HttpResponseRedirect(reverse("search", args=()))

	else:
		user_id = User.objects.get(pk=request.user.id)

		try:
			bio = str(request.POST.get("bio"))
		except KeyError:
			return render(request, "circle/error.html", context={"message":  "Enter a Bio.!!", "type": "Key Error", "link": "newPerson"})
		except ValueError:
			return render(request, "circle/error.html", context={"message": "Invalid Value to given field.!!", "type": "Value Error", "link": "newPerson"})
		except TypeError:
			return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error", "link": "newPerson"})

		try:
			first = str(request.POST.get("first"))
		except KeyError:
			return render(request, "circle/error.html", context={"message":  "Enter a First Name.!!", "type": "Key Error", "link": "newPerson"})
		except ValueError:
			return render(request, "circle/error.html", context={"message": "Invalid Value to given field.!!", "type": "Value Error", "link": "newPerson"})
		except TypeError:
			return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error", "link": "newPerson"})

		try:
			last = str(request.POST.get("last"))
		except KeyError:
			return render(request, "circle/error.html", context={"message":  "Enter a Last Name.!!", "type": "Key Error", "link": "newPerson"})
		except ValueError:
			return render(request, "circle/error.html", context={"message": "Invalid Value to given field.!!", "type": "Value Error", "link": "newPerson"})
		except TypeError:
			return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error", "link": "newPerson"})

		try:
			age = int(request.POST.get("age"))
		except KeyError:
			return render(request, "circle/error.html", context={"message": "Enter a Age!", "type": "Key Error.!!", "link": "newPerson"})
		except ValueError:
			return render(request, "circle/error.html", context={"message": "Invalid Value to given field.!!", "type": "Value Error", "link": "newPerson"})
		except TypeError:
			return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error", "link": "newPerson"})

		try:
			sex = str(request.POST.get("sex"))
		except KeyError:
			return render(request, "circle/error.html", context={"message": "Select gender from the options provided.!!", "type": "KeyError", "link": "newPerson"})
		except ValueError:
			return render(request, "circle/error.html", context={"message": "Invalid Value to given field.!!", "type": "Value Error", "link": "newPerson"})
		except TypeError:
			return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error", "link": "newPerson"})

		sex = sex[0]

		try:
			email = str(request.POST.get("email"))
		except KeyError:
			return render(request, "circle/error.html", context={"message": "Enter an e-mail address.!!", "type": "KeyError", "link": "newPerson"})
		except ValueError:
			return render(request, "circle/error.html", context={"message": "Invalid Value to given field.!!", "type": "Value Error", "link": "newPerson"})
		except TypeError:
			return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error", "link": "newPerson"})

		ph_no = (9378214503 + (user_id * 10) % request.user.id)

		try:
			ph_no = str(request.POST.get("ph_no"))
		except KeyError:
			return render(request, "circle/error.html", context={"message": "Enter an e-mail address.!!", "type": "KeyError", "link": "newPerson"})
		except ValueError:
			return render(request, "circle/error.html", context={"message": "Invalid Value to given field.!!", "type": "Value Error", "link": "newPerson"})
		except TypeError:
			return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error", "link": "newPerson"})

		username = email.split('@')[0]

		person = Person.objects.create(user=user_id, username=username, bio=bio, first=first, last=last, age=age, sex=sex, email=email, ph_no=ph_no)

		return HttpResponseRedirect(reverse("person", args=(person.id, )))


@login_required
def person(request, person_id):
	try:
		person = Person.objects.get(pk=person_id)
		return render(request, "circle/person.html", context={"person": person})
	except Person.DoesNotExist:
		return render(request, "circle/error.html", context={"message": "Person Does Not Exist.!!", "type": "Key Error.!", "link": "person"})


@login_required
def persons(request):
	persons = Person.objects.all()
	return render(request, "circle/persons.html", context={"persons": persons})


@login_required
def newArticle(request):
	form = ArticleForm()
	return render(request, "circle/newArticle.html", context={"form": form})


@login_required	
def addArticle(request):
	# if request.method == "POST":
	# 	cprint('post', 'cyan')
	# 	form = ArticleForm(request.POST, request.FILES)
	# 	cprint(form, 'yellow')
	# 	if form.is_valid():
	# 		cprint('yes', 'red')
	# 	form.save()
	# 	return HttpResponseRedirect(reverse("articles"))
	# else:
	# 	form = ArticleForm()
	# return render(request, "circle/newArticle.html", context={"form": form})

	if request.GET:
		return HttpResponseRedirect(reverse("newArticle", args=()))
	else:
		user_id = request.user.id

		try:
			title = str(request.POST.get("title"))
		except KeyError:
			return render(request, "circle/error.html", context={"message": "Enter title.!!", "type": "Key Error", "link": "newArticle"})
		except ValueError:
			return render(request, "circle/error.html", context={"message": "Invalid Value to given field.!!", "type": "Value Error", "link": "newArticle"})
		except TypeError:
			return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error", "link": "newArticle"})

		try:
			description =  str(request.POST.get('description'))
		except KeyError:
			return render(request, "circle/error.html", context={"message": "Enter description.!!", "type": "Key Error", "link": "newArticle"})
		except ValueError:
			return render(request, "circle/error.html", context={"message": "Invalid Value to given field.!!", "type": "Value Error", "link": "newArticle"})
		except TypeError:
			return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error", "link": "newArticle"})

		
		# try:
		image = request.FILES['image']
		cprint(image, 'red')
		# except KeyError:
			# return render(request, "circle/error.html", context={"message": "Upload file.!!", "type": "Key Error", "link": "newArticle"})
		# except ValueError:
			# return render(request, "circle/error.html", context={"message": "Invalid Value to given field image.!!", "type": "Value Error", "link": "newArticle"})
		# except TypeError:
			# return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error", "link": "newArticle"})


		try:
			price = float(request.POST.get('price'))
		except KeyError:
			return render(request, "circle/error.html", context={"message": "Enter price.!!", "type": "Key Error", "link": "newArticle"})
		except ValueError:
			return render(request, "circle/error.html", context={"message": "Invalid Value to given field.!!", "type": "Value Error", "link": "newArticle"})
		except TypeError:
			return render(request, "circle/error.html", context={"message": "Incompatible Tag DataType.!!", "type": "Type Error", "link": "newArticle"})


		try:
			tags = request.POST.get('tags')
			if tags is not None:
				tags = list(tags)
			else:
				tags = []
		except KeyError:
			return render(request, "circle/error.html", context={"message": "Enter title.!!", "type": "Key Error", "link": "newArticle"})
		except ValueError:
			return render(request, "circle/error.html", context={"message": "Invalid Value to given field.!!", "type": "Value Error", "link": "newArticle"})
		except TypeError:
			return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error", "link": "newArticle"})

		article = Article.objects.create(title=title, description=description, image=image, price=price)
		# cprint(article, 'red')

		# pub_ts = article.pub_ts
		# cprint(pub_ts, 'white')

		# article.image = set_unique_name(article.image.url, pub_ts)
		# cprint(article.image.url, 'blue')

		# for tag in tags:
		# 	article.tags.add(tag)

		try:
			person = Person.objects.filter(user_id=user_id).first()
			person.display.add(article)
			person.save() 
			return HttpResponseRedirect(reverse("article", args=(article.id, )))
		except Person.DoesNotExist:  
			return render(request, "circle/error.html", context={"message": "No person found.!!", "type": "Key Error", "link": "newArticle"})

@login_required
def article(request, article_id):
	try:
		article = Article.objects.get(pk=article_id)
	except Article.DoesNotExist:
		return render(request, "circle/error.html", context={"message": "Article does not exist.!!", "type": "Type Error", "link": "search"})
	tags = article.tags.all()
	try:
		not_tagged = Article.objects.exclude(tags=tags)
	except Tag.DoesNotExist:
		not_tagged = []
	return render(request, "circle/article.html", context={"article": article, "not_tagged": not_tagged})


@login_required
def articles(request):
	articles = Article.objects.all()
	return render(request, "circle/articles.html", context={"articles": articles})

# testing left
@login_required
def friends(request):
	user_id = request.user.id
	try:
		person = Person.objects.filter(user_id=user_id)
		friends = person.friends.all()
		return render(request, "circle/friends.html", context={"friends": friends})
	except Person.DoesNotExist:
		friends = []
		return render(request, "circle/error.html", context={"message": "You don't have any friends.!!", "type": "Type Error", "link": "search"})


#testing left
@login_required
def update(request):
	user_id = request.user.id

	if request.POST:
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
		except User.DoesNotExist:
			return render(request, "circle/error.html", context={"message": "User Doesn't Exist!", "type": "Value DoesNotExist.!!", "link": "search"})

	return render(request, "circle/user.html", context={"user": user})


@login_required
def search(request):
	return render(request, "circle/search.html", context={})


@login_required
def result(request):
	if request.GET:
		return HttpResponseRedirect(reverse('search', args=()))
	else:
		try:
			search = str(request.POST.get("search"))
		except KeyError:
			return render(request, "circle/error.html", context={"message":  "Enter a Bio.!!", "type": "Key Error", "link": "articles"})
		except ValueError:
			return render(request, "circle/error.html", context={"message": "Invalid Value to given field.!!", "type": "Value Error", "link": "articles"})
		except TypeError:
			return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error", "link": "articles"})

	articles = Article.objects.filter(Q(title__contains=search) | Q(description__contains=search))

	return render(request, "circle/result.html", context={'articles': articles})


# testing left
@login_required
def display(request):
	try:
		user_id = request.user.id
		person = Person.objects.filter(user_id=user_id).first()
		articles = person.display.all()
		return render(request, "circle/display.html", context={"articles": articles})
	except Person.DoesNotExist:
		return render(request, "circle/error.html", context={"message": "No Person Found.!!", "type": "Type Error", "link": "search"})


# testing left
@login_required
def bookmark(request, article_id):
	try:
		user_id = request.user.id
		article = Article.objects.get(pk=article_id)
		person = Person.objects.filter(user_id=user_id).first()
		cprint(person, 'white')
		person.bookmarked.add(article)
		person.save()
		return HttpResponseRedirect(reverse("wishlisted", args=()))
	except Article.DoesNotExist:
		return render(request, "circle/error.html", context={"message": "No Article Found.!!", "type": "Type Error", "link": "search"})
	except Person.DoesNotExist:
		return render(request, "circle/error.html", context={"message": "No Person Found.!!", "type": "Type Error", "link": "search"})

#testing left
@login_required
def rent(request, article_id):
	try:
		user_id = request.user.id
		article = Article.objects.get(pk=article_id)
		person = Person.objects.filter(user_id=user_id).first()
		person.rented.add(article)
		person.save()
		return HttpResponseRedirect(reverse("rented", args=()))
	except Article.DoesNotExist:
		return render(request, "circle/error.html", context={"message": "No Article Found.!!", "type": "Type Error", "link": "search"})
	except Person.DoesNotExist:
		return render(request, "circle/error.html", context={"message": "No Person Found.!!", "type": "Type Error", "link": "search"})

#testing left
@login_required
def buy(request, article_id):
	try:
		user_id = request.user.id
		article = Article.objects.get(pk=article_id)
		person = Person.objects.filter(user_id=user_id).first()
		person.carted.add(article)
		person.save()
		# user_id = article.user.id
		person = Person.objects.filter(display=article).first()
		person.sold.add(article)
		person.save()
		return HttpResponseRedirect(reverse("carted", args=()))
	except Article.DoesNotExist:
		return render(request, "circle/error.html", context={"message": "No Article Found.!!", "type": "Type Error", "link": "search"})
	except Person.DoesNotExist:
		return render(request, "circle/error.html", context={"message": "No Person Found.!!", "type": "Type Error", "link": "search"})

#testing left
@login_required
def purchased(request):
	try:
		user_id = request.user.id
		person = Person.objects.filter(user_id=user_id).first()
		articles = person.purchased.all()
		return render(request, "circle/wishlist.html", context={"articles": articles})
	except Person.DoesNotExist:
		return render(request, "circle/error.html", context={"message": "No Person Found.!!", "type": "Type Error", "link": "search"})

#testing left
def sold(request):
	try:
		user_id = request.user.id
		person = Person.objects.filter(user_id=user_id).first()
		articles = person.sold.all()
		return render(request, "circle/sold.html", context={"articles": articles})
	except Person.DoesNotExist:
		return render(request, "circle/error.html", context={"message": "No Person Found.!!", "type": "Type Error", "link": "search"})

# testing left
@login_required
def wishlisted(request):
	try:
		user_id = request.user.id
		person = Person.objects.filter(user_id=user_id).first()
		articles = person.bookmarked.all()
		return render(request, "circle/wishlist.html", context={"articles": articles})
	except Person.DoesNotExist:
		return render(request, "circle/error.html", context={"message": "No Person Found.!!", "type": "Type Error", "link": "search"})

#testing left
@login_required
def rented(request):
	try:
		user_id = request.user.id
		person = Person.objects.filter(user_id=user_id).first()
		articles = person.rented.all()
		return render(request, "circle/rented.html", context={"articles": articles})
	except Article.DoesNotExist:
		return render(request, "circle/error.html", context={"message": "No Article Found.!!", "type": "Type Error", "link": "search"})
	except Person.DoesNotExist:
		return render(request, "circle/error.html", context={"message": "No Person Found.!!", "type": "Type Error", "link": "search"})


@login_required
def carted(request):
	try:
		user_id = request.user.id
		person = Person.objects.filter(user_id=user_id).first()
		articles = person.carted.all()
		return render(request, "circle/cart.html", context={"articles": articles})
	except Article.DoesNotExist:
		return render(request, "circle/error.html", context={"message": "No Article Found.!!", "type": "Type Error", "link": "search"})
	except Person.DoesNotExist:
		return render(request, "circle/error.html", context={"message": "No Person Found.!!", "type": "Type Error", "link": "search"})


@login_required
def remove(request, article_id, type):
	try:
		user_id = request.user.id
		article = Article.objects.get(pk=article_id)
		if type == 'article':
			article.delete()
			return HttpResponseRedirect(reverse("articles", args=()))

		person = Person.objects.filter(user_id=user_id).first()			
		if type == 'marked':
			person.bookmarked.remove(article)
			person.save()
			return HttpResponseRedirect(reverse("wishlisted", args=()))
		elif type == 'rented':
			person.rented.remove(article)
			person.save()
			return HttpResponseRedirect(reverse("rented", args=()))
		elif type == 'carted':
			person.carted.remove(article)
			person.save()
			return HttpResponseRedirect(reverse("carted", args=()))
		else:
			return HttpResponseRedirect(reverse("search", args=()))
	except Article.DoesNotExist:
		return render(request, "circle/error.html", context={"message": "No Article Found.!!", "type": "Type Error", "link": "search"})
	except Person.DoesNotExist:
		return render(request, "circle/error.html", context={"message": "No Person Found.!!", "type": "Type Error", "link": "search"})


@login_required
def addMessage(request, chat_id):
	if request.POST:
		try:
			message = str(request.POST.get("message"))
			text = Message.objects.create(text=message)
			if text.isValidMessage():
				try:
					chat = Chat.objects.get(pk=chat_id)
					chat.messages.add(text)
					chat.save()
					return HttpResponseRedirect(reverse('chat', args=(chat_id, )))
				except Chat.DoesNotExist:
					return render(request, "circle/error.html", context={"message": "No Chat Found.!!", "type": "Type Error", "link": "chats"})
			else:
				return HttpResponse('Message Cannot be Empty.!')
		except KeyError:
			return render(request, "circle/error.html", context={"message": "Enter text.!!", "type": "Key Error", "link": "articles"})
		except ValueError:
			return render(request, "circle/error.html", context={"message": "Invalid Value to given field.!!", "type": "Value Error", "link": "articles"})
		except TypeError:
			return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error", "link": "articles"})
	else:
		return HttpResponseRedirect(reverse('home', args=()))
	
		
@login_required
def chat(request, chat_id):
	try:
		chat = Chat.objects.get(pk=chat_id)
		form = MessageForm()
		return render(request, "circle/chat.html", context={"chat": chat, "form": form})
	except Chat.DoesNotExist:
		return render(request, "circle/error.html", context={"message": "No Chat Found.!!", "type": "Type Error", "link": "chats"})


@login_required
def chats(request):
	chats = Chat.objects.all()
	return render(request, "circle/chats.html", context={"chats": chats})


# testing left
@login_required
def message(request):

	if request.POST:
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


@login_required
def user(request, user_id):
	try:
		user = User.objects.get(pk=user_id)
		return render(request, "circle/user.html", context={"user": user})
	except User.DoesNotExist:
		return render(request, "circle/error.html", context={"message": "User Doesn't Exist!!", "type": "Value DoesNotExist!!", "link": "users"})


@login_required
def users(request):
	users = User.objects.all()
	return render(request, "circle/users.html", context={"users": users})


@login_required
def error(request):
	return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error", "link": "home"})
