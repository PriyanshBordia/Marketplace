from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404

from .models import Article, Person, Message, Tag

# Create your views here.

# @login_required(login_url='login')
def home(request):
    return render(request, "circle/home.html", context={})


def addPerson(request):

	user_id = User.objects.get(pk=request.user.id)

	try:
		bio = str(request.POST.get("bio"))
	except KeyError:
		return render(request, "circle/error.html", context={"message":  "Enter a Bio.!!", "type": "Key Error"})
	except ValueError:
		return render(request, "circle/error.html", context={"message": "Invalid Value to given field.!!", "type": "Value Error"})
	except TypeError:
		return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error"})

	try:
		first = str(request.POST.get("first"))
	except KeyError:
		return render(request, "circle/error.html", context={"message":  "Enter a First Name.!!", "type": "Key Error"})
	except ValueError:
		return render(request, "circle/error.html", context={"message": "Invalid Value to given field.!!", "type": "Value Error"})
	except TypeError:
		return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error"})

	try:
		last = str(request.POST.get("last"))
	except KeyError:
		return render(request, "circle/error.html", context={"message":  "Enter a Last Name.!!", "type": "Key Error"})
	except ValueError:
		return render(request, "circle/error.html", context={"message": "Invalid Value to given field.!!", "type": "Value Error"})
	except TypeError:
		return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error"})

	try:
		age = int(request.POST.get("age"))
	except KeyError:
		return render(request, "circle/error.html", context={"message": "Enter a Age!", "type": "Key Error.!!"})
	except ValueError:
		return render(request, "circle/error.html", context={"message": "Invalid Value to given field.!!", "type": "Value Error"})
	except TypeError:
		return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error"})

	try:
		sex = str(request.POST.get("sex"))
	except KeyError:
		return render(request, "circle/error.html", context={"message": "Select appropriate gender from the options provided.!!", "type": "KeyError"})
	except ValueError:
		return render(request, "circle/error.html", context={"message": "Invalid Value to given field.!!", "type": "Value Error"})
	except TypeError:
		return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error"})

	sex = sex[0]

	try:
		email = str(request.POST.get("email"))
	except KeyError:
		return render(request, "circle/error.html", context={"message": "Enter an e-mail address.!!", "type": "KeyError"})
	except ValueError:
		return render(request, "circle/error.html", context={"message": "Invalid Value to given field.!!", "type": "Value Error"})
	except TypeError:
		return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error"})

	ph_no = (9378214503 + (user_id * 10) % request.user.id)

	username = email.split('@')[0]

	person = Person(username=username, bio=bio, first=first, last=last, age=age, sex=sex, email=email, ph_no=ph_no)

	person.save()

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
		return render(request, "circle/error.html", context={"message": "Enter title.!!", "type": "Key Error"})
	except ValueError:
		return render(request, "circle/error.html", context={"message": "Invalid Value to given field.!!", "type": "Value Error"})
	except TypeError:
		return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error"})

	try:
		description =  str(request.get('description'))
	except KeyError:
		return render(request, "circle/error.html", context={"message": "Enter title.!!", "type": "Key Error"})
	except ValueError:
		return render(request, "circle/error.html", context={"message": "Invalid Value to given field.!!", "type": "Value Error"})
	except TypeError:
		return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error"})

	
	try:
		image = request.get('image')
	except KeyError:
		return render(request, "circle/error.html", context={"message": "Enter title.!!", "type": "Key Error"})
	except ValueError:
		return render(request, "circle/error.html", context={"message": "Invalid Value to given field.!!", "type": "Value Error"})
	except TypeError:
		return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error"})


	try:
		price = float(request.get('price'))
	except KeyError:
		return render(request, "circle/error.html", context={"message": "Enter title.!!", "type": "Key Error"})
	except ValueError:
		return render(request, "circle/error.html", context={"message": "Invalid Value to given field.!!", "type": "Value Error"})
	except TypeError:
		return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error"})


	try:
		tags = list(request.get('tags'))
	except KeyError:
		return render(request, "circle/error.html", context={"message": "Enter title.!!", "type": "Key Error"})
	except ValueError:
		return render(request, "circle/error.html", context={"message": "Invalid Value to given field.!!", "type": "Value Error"})
	except TypeError:
		return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error"})
	
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
	try:
		search = str(request.POST.get("search"))
	except KeyError:
		return render(request, "circle/error.html", context={"message":  "Enter a Bio.!!", "type": "Key Error"})
	except ValueError:
		return render(request, "circle/error.html", context={"message": "Invalid Value to given field.!!", "type": "Value Error"})
	except TypeError:
		return render(request, "circle/error.html", context={"message": "Incompatible DataType.!!", "type": "Type Error", })

	return render(request, "circle/search.html", context={})


def result(request):
    articles = Article.objects.all()
    return render(request, "circle/result.html", context={'articles': articles})


def user(request):
    return render(request, "circle/user.html", context={})


def update(request):
    return render(request, "circle/user.html", context={})


def message(request, sender_id, receiver_id):
    return render(request, "circle/home.html", context={})

def login(request):
	pass

def logout(request):
	pass