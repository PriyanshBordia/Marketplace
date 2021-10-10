import os

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import ArticleForm
from .forms import ChatForm
from .forms import MessageForm
from .forms import PersonForm
from .forms import TagForm
from .models import Article
from .models import Chat
from .models import Message
from .models import Person
from .models import Tag
from .utils import *

# Create your views here.


def home(request):
    return render(request, "circle/home.html", context={})


@login_required
def newPerson(request):
    form = PersonForm()
    tags = Tag.objects.all()
    return render(
        request, "circle/newPerson.html", context={"form": form, "tags": tags}
    )


@login_required
def addPerson(request):
    try:
        person = Person()
        if request.POST:
            form = PersonForm(request.POST, request.FILES, instance=person)
            if form.is_valid():
                person.user = User.objects.get(pk=request.user.id)
                person.username = str(form.cleaned_data["email"].split("@")[0])
                email = person.email
                if Person.objects.filter(email=email).exists():
                    return render(
                        request,
                        "circle/error.html",
                        context={
                            "message": "Email Already Registered.!!",
                            "type": "Integrity Error",
                            "link": "newPerson",
                        },
                    )
                form.save()
                print(person)
                Chat.objects.create(left=person, right=person)
                return HttpResponseRedirect(reverse("person", args=(person.id,)))
            return render(
                request,
                "circle/error.html",
                context={
                    "message": "Invalid Data.!!",
                    "type": "Type Error",
                    "link": "search",
                },
            )
        form = PersonForm(instance=person)
        return render(
            request, "circle/person.html", context={"person": person, "form": form}
        )
    except Exception as e:
        return render(
            request,
            "circle/error.html",
            context={"message": str(e), "type": "Internal Error", "link": "newPerson"},
        )


@login_required
def person(request, person_id):
    try:
        person = Person.objects.get(pk=person_id)
        if Person.objects.filter(
            pk=request.user.person.id, friends__pk=person.id
        ).exists():
            if Chat.objects.filter(
                Q(left=person_id, right=request.user.person.id)
                | Q(left=request.user.person.id, right=person_id)
            ).exists():
                chat_id = (
                    Chat.objects.filter(
                        Q(left=person_id, right=request.user.person.id)
                        | Q(left=request.user.person.id, right=person_id)
                    )
                    .first()
                    .id
                )
                return render(
                    request,
                    "circle/person.html",
                    context={"person": person, "chat_id": chat_id},
                )
        else:
            return render(request, "circle/person.html", context={"person": person})
    except Person.DoesNotExist:
        return render(
            request,
            "circle/error.html",
            context={
                "message": "Person Does Not Exist.!!",
                "type": "Data Error.!",
                "link": "search",
            },
        )
    except Chat.DoesNotExist:
        return render(
            request,
            "circle/error.html",
            context={
                "message": "No Chat Found.!!",
                "type": "Data Error.!",
                "link": "search",
            },
        )


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
    article = Article()
    try:
        if request.method == "POST":
            form = ArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid():
                try:
                    form.save()
                    person = Person.objects.get(pk=request.user.person.id)
                    person.display.add(article)
                    person.save()
                    return HttpResponseRedirect(reverse("article", args=(article.id,)))
                except Person.DoesNotExist:
                    return render(
                        request,
                        "circle/error.html",
                        context={
                            "message": "No person found.!!",
                            "type": "Data Error",
                            "link": "newArticle",
                        },
                    )
            else:
                return render(
                    request,
                    "circle/error.html",
                    context={
                        "message": "Invalid Data.!!",
                        "type": "Type Error",
                        "link": "search",
                    },
                )
        else:
            form = ArticleForm(instance=article)
            return render(
                request,
                "circle/article.html",
                context={"article": article, "form": form},
            )
    except Exception as e:
        return render(
            request,
            "circle/error.html",
            context={"message": str(e), "type": "Internal Error", "link": "newArticle"},
        )


@login_required
def edit(request, id, type):
    if type == "person":
        try:
            person = Person.objects.get(pk=id)
            if request.POST:
                form = PersonForm(request.POST, request.FILES, instance=person)
                if form.is_valid():
                    person.username = str(form.cleaned_data["email"].split("@")[0])
                    email = str(form.cleaned_data["email"])
                    if (
                        Person.objects.filter(email=email)
                        .exclude(pk=person.id)
                        .exists()
                    ):
                        return render(
                            request,
                            "circle/error.html",
                            context={
                                "message": "Email Already Registered.!!",
                                "type": "Integrity Error",
                                "link": "newPerson",
                            },
                        )
                    form.save()
                    return HttpResponseRedirect(reverse("person", args=(person.id,)))
                else:
                    return render(
                        request,
                        "circle/error.html",
                        context={
                            "message": "Invalid Data.!!",
                            "type": "Type Error",
                            "link": "search",
                        },
                    )
            else:
                form = PersonForm(instance=person)
                return render(
                    request,
                    "circle/person.html",
                    context={"person": person, "form": form},
                )
        except Person.DoesNotExist:
            return render(
                request,
                "circle/error.html",
                context={
                    "message": "No Person Found.!!",
                    "type": "Type Error",
                    "link": "search",
                },
            )

    elif type == "article":
        try:
            article = Article.objects.get(pk=id)
            if request.POST:
                form = ArticleForm(request.POST, request.FILES, instance=article)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect(reverse("article", args=(id,)))
                return render(
                    request,
                    "circle/error.html",
                    context={
                        "message": "Invalid Data.!!",
                        "type": "Type Error",
                        "link": "articles",
                    },
                )
            form = ArticleForm(instance=article)
            return render(
                request,
                "circle/article.html",
                context={"article": article, "form": form},
            )
        except Article.DoesNotExist:
            return render(
                request,
                "circle/error.html",
                context={
                    "message": "No Article Found.!!",
                    "type": "Type Error",
                    "link": "articles",
                },
            )

    elif type == "tag":
        try:
            tag = Tag.objects.get(pk=id)
            if request.POST:
                form = TagForm(request.POST, request.FILES, instance=tag)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect(reverse("tag", args=(id,)))
                return render(
                    request,
                    "circle/error.html",
                    context={
                        "message": "Invalid Data.!!",
                        "type": "Type Error",
                        "link": "tags",
                    },
                )
            form = TagForm(instance=tag)
            return render(
                request, "circle/tag.html", context={"tag": tag, "form": form}
            )
        except Tag.DoesNotExist:
            return render(
                request,
                "circle/error.html",
                context={
                    "message": "No Tag Found.!!",
                    "type": "Type Error",
                    "link": "tags",
                },
            )
    return render(
        request,
        "circle/error.html",
        context={"message": "Invalid Type.!!", "type": "Type Error", "link": "search"},
    )


@login_required
def article(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        return render(
            request,
            "circle/error.html",
            context={
                "message": "Article does not exist.!!",
                "type": "Type Error",
                "link": "search",
            },
        )
    tags = article.tags.all()
    try:
        not_tagged = Article.objects.exclude(tags=tags)
    except Tag.DoesNotExist:
        not_tagged = []
    return render(
        request,
        "circle/article.html",
        context={"article": article, "not_tagged": not_tagged},
    )


@login_required
def articles(request):
    articles = Article.objects.all()
    return render(request, "circle/articles.html", context={"articles": articles})


@login_required
def addTag(request):
    tag = Tag()
    try:
        if request.method == "POST":
            form = TagForm(request.POST, request.FILES, instance=tag)
            if form.is_valid():
                try:
                    form.save()
                    person = Person.objects.get(pk=request.user.person.id)
                    person.tags.add(tag)
                    person.save()
                    return HttpResponseRedirect(reverse("tag", args=(tag.id,)))
                except Person.DoesNotExist:
                    return render(
                        request,
                        "circle/error.html",
                        context={
                            "message": "No person found.!!",
                            "type": "Data Error",
                            "link": "newArticle",
                        },
                    )
            else:
                return render(
                    request,
                    "circle/error.html",
                    context={
                        "message": "Invalid Data.!!",
                        "type": "Type Error",
                        "link": "search",
                    },
                )
        else:
            form = TagForm(instance=tag)
            return render(
                request, "circle/addTag.html", context={"tag": tag, "form": form}
            )
    except Exception as e:
        return render(
            request,
            "circle/error.html",
            context={"message": str(e), "type": "Internal Error", "link": "addTag"},
        )


@login_required
def tag(request, tag_id):
    try:
        tag = Tag.objects.get(pk=tag_id)
        return render(request, "circle/tag.html", context={"tag": tag})
    except Tag.DoesNotExist:
        return render(
            request,
            "circle/error.html",
            context={
                "message": "Tag does not exist.!!",
                "type": "Type Error",
                "link": "search",
            },
        )


@login_required
def tags(request):
    tags = Tag.objects.all()
    return render(request, "circle/tags.html", context={"tags": tags})


@login_required
def addFriend(request, person_id):
    try:
        friend = Person.objects.get(pk=person_id)
        person = Person.objects.get(pk=request.user.person.id)
        person.friends.add(friend)
        person.save()
        if friend.allowsMessage:
            Chat.objects.create(left=person, right=friend)
        return HttpResponseRedirect(reverse("person", args=(person.id,)))
    except Person.DoesNotExist:
        return render(
            request,
            "circle/error.html",
            context={
                "message": "No person found.!!",
                "type": "Data Error",
                "link": "search",
            },
        )


@login_required
def friends(request):
    try:
        person_id = request.user.person.id
        person = Person.objects.get(pk=person_id)
        friends = person.friends.all()
        chats = Chat.objects.filter(Q(left=person) | Q(right=person))
        return render(
            request, "circle/friends.html", context={"chats": chats, "friends": friends}
        )
    except Person.DoesNotExist:
        return render(
            request,
            "circle/error.html",
            context={
                "message": "You don't have any friends.!!",
                "type": "Data Error",
                "link": "search",
            },
        )
    except Chat.DoesNotExist:
        return render(
            request,
            "circle/error.html",
            context={
                "message": "You don't have any chats.!!",
                "type": "Data Error",
                "link": "search",
            },
        )


@login_required
def search(request, type):
    if type != "article" and type != "person":
        type = "article"
    return render(request, "circle/search.html", context={"type": type})


@login_required
def result(request, type):
    try:
        if request.GET:
            return HttpResponseRedirect(reverse("search", args=(type,)))
        try:
            search = str(request.POST.get("search"))
        except KeyError:
            return render(
                request,
                "circle/error.html",
                context={
                    "message": "Enter text to search.!!",
                    "type": "Key Error",
                    "link": "search",
                },
            )
        except ValueError:
            return render(
                request,
                "circle/error.html",
                context={
                    "message": "Invalid Value to given field.!!",
                    "type": "Value Error",
                    "link": "search",
                },
            )
        except TypeError:
            return render(
                request,
                "circle/error.html",
                context={
                    "message": "Incompatible DataType.!!",
                    "type": "Type Error",
                    "link": "search",
                },
            )

            if type == "article":
                # .values_list('id'))
                display = list(
                    Person.objects.get(pk=request.user.person.id).display.all()
                )
                # .values_list('id'))
                rent = list(Person.objects.get(pk=request.user.person.id).rented.all())
                # .values_list('id'))
                purchased = list(
                    Person.objects.get(pk=request.user.person.id).purchased.all()
                )
                # .values_list('id'))
                sold = list(Person.objects.get(pk=request.user.person.id).sold.all())
                # cprint(display, 'green')
                # cprint(rent, 'red')
                # cprint(purchased, 'blue')
                # cprint(sold, 'yellow')

                articles = Article.objects.filter(
                    Q(title__contains=search) | Q(description__contains=search)
                )
                # .exclude(display)
                # .exclude(rent).exclude(purchased).exclude(sold)
                return render(
                    request,
                    "circle/result.html",
                    context={"articles": articles, "type": type},
                )
            if type == "person":
                friends = list(
                    Person.objects.get(pk=request.user.person.id).friends.all()
                )
                persons = Person.objects.filter(
                    Q(first__contains=search)
                    | Q(last__contains=search)
                    | Q(username__contains=search)
                ).exclude(friends__in=friends)
                return render(
                    request,
                    "circle/result.html",
                    context={"persons": persons, "type": type},
                )
    except Article.DoesNotExist:
        return render(
            request,
            "circle/error.html",
            context={
                "message": "No Article Found.!!",
                "type": "Type Error",
                "link": "search",
            },
        )
    except Person.DoesNotExist:
        return render(
            request,
            "circle/error.html",
            context={
                "message": "No Person Found.!!",
                "type": "Type Error",
                "link": "search",
            },
        )


@login_required
def display(request):
    try:
        person_id = request.user.person.id
        person = Person.objects.get(pk=person_id)
        articles = person.display.all()
        return render(request, "circle/display.html", context={"articles": articles})
    except Person.DoesNotExist:
        return render(
            request,
            "circle/error.html",
            context={
                "message": "No Person Found.!!",
                "type": "Type Error",
                "link": "search",
            },
        )


@login_required
def wishlist(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
        person_id = request.user.person.id
        person = Person.objects.get(pk=person_id)
        person.bookmarked.add(article)
        person.save()
        return HttpResponseRedirect(reverse("wishlisted", args=()))
    except Article.DoesNotExist:
        return render(
            request,
            "circle/error.html",
            context={
                "message": "No Article Found.!!",
                "type": "Type Error",
                "link": "search",
            },
        )
    except Person.DoesNotExist:
        return render(
            request,
            "circle/error.html",
            context={
                "message": "No Person Found.!!",
                "type": "Type Error",
                "link": "search",
            },
        )


@login_required
def rent(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
        person_id = request.user.person.id
        person = Person.objects.get(pk=person_id)
        if article not in person.purchased.all():
            person.rented.add(article)
            person.save()
            return HttpResponseRedirect(reverse("rented", args=()))
        return HttpResponseRedirect(reverse("article", args=(article_id,)))
    except Article.DoesNotExist:
        return render(
            request,
            "circle/error.html",
            context={
                "message": "No Article Found.!!",
                "type": "Type Error",
                "link": "search",
            },
        )
    except Person.DoesNotExist:
        return render(
            request,
            "circle/error.html",
            context={
                "message": "No Person Found.!!",
                "type": "Type Error",
                "link": "search",
            },
        )


@login_required
def retreat(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
        person_id = request.user.person.id
        person = Person.objects.get(pk=person_id)
        person.retreated.add(article)
        person.rented.remove(article)
        person.save()
        return HttpResponseRedirect(reverse("rented", args=()))
    except Article.DoesNotExist:
        return render(
            request,
            "circle/error.html",
            context={
                "message": "No Article Found.!!",
                "type": "Type Error",
                "link": "search",
            },
        )
    except Person.DoesNotExist:
        return render(
            request,
            "circle/error.html",
            context={
                "message": "No Person Found.!!",
                "type": "Type Error",
                "link": "search",
            },
        )


@login_required
def cart(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
        person_id = request.user.person.id
        person = Person.objects.get(pk=person_id)
        if article not in person.purchased.all():
            person.carted.add(article)
            person.save()
        return HttpResponseRedirect(reverse("carted", args=()))
    except Article.DoesNotExist:
        return render(
            request,
            "circle/error.html",
            context={
                "message": "No Article Found.!!",
                "type": "Data Error",
                "link": "search",
            },
        )
    except Person.DoesNotExist:
        return render(
            request,
            "circle/error.html",
            context={
                "message": "No Person Found.!!",
                "type": "Data Error",
                "link": "search",
            },
        )


@login_required
def buy(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
        person_id = request.user.person.id
        person = Person.objects.get(pk=person_id)
        if article not in person.rented.all() and article not in person.purchased.all():
            person.purchased.add(article)
            person.carted.remove(article)
            person.save()
        return HttpResponseRedirect(reverse("purchased", args=()))
    except Article.DoesNotExist:
        return render(
            request,
            "circle/error.html",
            context={
                "message": "No Article Found.!!",
                "type": "Data Error",
                "link": "search",
            },
        )
    except Person.DoesNotExist:
        return render(
            request,
            "circle/error.html",
            context={
                "message": "No Person Found.!!",
                "type": "Data Error",
                "link": "search",
            },
        )


@login_required
def purchased(request):
    try:
        person_id = request.user.person.id
        person = Person.objects.get(pk=person_id)
        articles = person.purchased.all()
        return render(request, "circle/purchased.html", context={"articles": articles})
    except Person.DoesNotExist:
        return render(
            request,
            "circle/error.html",
            context={
                "message": "No Person Found.!!",
                "type": "Type Error",
                "link": "search",
            },
        )


@login_required
def sold(request):
    try:
        person_id = request.user.person.id
        person = Person.objects.get(pk=person_id)
        articles = person.sold.all()
        return render(request, "circle/sold.html", context={"articles": articles})
    except Person.DoesNotExist:
        return render(
            request,
            "circle/error.html",
            context={
                "message": "No Person Found.!!",
                "type": "Type Error",
                "link": "search",
            },
        )


@login_required
def wishlisted(request):
    try:
        person_id = request.user.person.id
        person = Person.objects.get(pk=person_id)
        articles = person.bookmarked.all()
        return render(request, "circle/wishlist.html", context={"articles": articles})
    except Person.DoesNotExist:
        return render(
            request,
            "circle/error.html",
            context={
                "message": "No Person Found.!!",
                "type": "Type Error",
                "link": "search",
            },
        )


@login_required
def rented(request):
    try:
        person_id = request.user.person.id
        person = Person.objects.get(pk=person_id)
        articles = person.rented.all()
        return render(request, "circle/rent.html", context={"articles": articles})
    except Article.DoesNotExist:
        return render(
            request,
            "circle/error.html",
            context={
                "message": "No Article Found.!!",
                "type": "Type Error",
                "link": "search",
            },
        )
    except Person.DoesNotExist:
        return render(
            request,
            "circle/error.html",
            context={
                "message": "No Person Found.!!",
                "type": "Type Error",
                "link": "search",
            },
        )


@login_required
def carted(request):
    try:
        person_id = request.user.person.id
        person = Person.objects.get(pk=person_id)
        articles = person.carted.all()
        return render(request, "circle/cart.html", context={"articles": articles})
    except Article.DoesNotExist:
        return render(
            request,
            "circle/error.html",
            context={
                "message": "No Article Found.!!",
                "type": "Type Error",
                "link": "search",
            },
        )
    except Person.DoesNotExist:
        return render(
            request,
            "circle/error.html",
            context={
                "message": "No Person Found.!!",
                "type": "Type Error",
                "link": "search",
            },
        )


@login_required
def retreated(request):
    try:
        person_id = request.user.person.id
        person = Person.objects.get(pk=person_id)
        articles = person.retreated.all()
        return render(request, "circle/retreat.html", context={"articles": articles})
    except Article.DoesNotExist:
        return render(
            request,
            "circle/error.html",
            context={
                "message": "No Article Found.!!",
                "type": "Type Error",
                "link": "search",
            },
        )
    except Person.DoesNotExist:
        return render(
            request,
            "circle/error.html",
            context={
                "message": "No Person Found.!!",
                "type": "Type Error",
                "link": "search",
            },
        )


@login_required
def remove(request, id, type):
    if type == "person":
        try:
            person = Person.objects.get(pk=id)
            person.delete()
            return HttpResponseRedirect(reverse("search", args=("person",)))
        except Person.DoesNotExist:
            return render(
                request,
                "circle/error.html",
                context={
                    "message": "No Person Found.!!",
                    "type": "Type Error",
                    "link": "search",
                },
            )
    elif type == "friend":
        try:
            friend = Person.objects.get(pk=id)
            person_id = request.user.person.id
            person = Person.objects.get(pk=person_id)
            person.friends.remove(friend)
            return HttpResponseRedirect(reverse("person", args=(person_id,)))
        except Person.DoesNotExist:
            return render(
                request,
                "circle/error.html",
                context={
                    "message": "No Person Found.!!",
                    "type": "Data Error",
                    "link": "search",
                },
            )
    elif type == "chat":
        try:
            chat = Chat.objects.get(pk=id)
            person_id = request.user.person.id
            person = Person.objects.get(pk=person_id)
            chats.objects.delete(chat)
            return HttpResponseRedirect(reverse("person", args=(person_id,)))
        except Chat.DoesNotExist:
            return render(
                request,
                "circle/error.html",
                context={
                    "message": "No Person Found.!!",
                    "type": "Data Error",
                    "link": "search",
                },
            )
    else:
        try:
            person_id = request.user.person.id
            article = Article.objects.get(pk=id)
            if type == "article":
                article.delete()
                return HttpResponseRedirect(reverse("articles", args=()))
            person = Person.objects.get(pk=person_id)
            if type == "marked":
                person.bookmarked.remove(article)
                person.save()
                return HttpResponseRedirect(reverse("wishlisted", args=()))
            if type == "rented":
                person.rented.remove(article)
                person.save()
                return HttpResponseRedirect(reverse("rented", args=()))
            if type == "carted":
                person.carted.remove(article)
                person.save()
                return HttpResponseRedirect(reverse("carted", args=()))
            # elif type == 'purchased':
            # 	person.purchased.remove(article)
            # 	person.save()
            # 	return HttpResponseRedirect(reverse('purchased', args=()))
            if type == "display":
                person.display.remove(article)
                person.save()
                article.delete()
                return HttpResponseRedirect(reverse("display", args=()))
            return HttpResponseRedirect(reverse("search", args=("article",)))
        except Article.DoesNotExist:
            return render(
                request,
                "circle/error.html",
                context={
                    "message": "No Article Found.!!",
                    "type": "Type Error",
                    "link": "search",
                },
            )
        except Person.DoesNotExist:
            return render(
                request,
                "circle/error.html",
                context={
                    "message": "No Person Found.!!",
                    "type": "Type Error",
                    "link": "search",
                },
            )


@login_required
def addMessage(request, chat_id):
    try:
        if request.POST:
            message = str(request.POST.get("message"))
            chat = Chat.objects.get(pk=chat_id)
            sender = Person.objects.get(pk=request.user.person.id)
            if sender.id == chat.left.id:
                receiver_id = chat.right.id
            else:
                receiver_id = chat.left.id
            receiver = Person.objects.get(pk=receiver_id)
            text = Message.objects.create(
                sender=sender, receiver=receiver, text=message
            )
            if text.isValidMessage():
                try:
                    chat.messages.add(text)
                    chat.save()
                    return HttpResponseRedirect(reverse("chat", args=(chat_id,)))
                except Chat.DoesNotExist:
                    return render(
                        request,
                        "circle/error.html",
                        context={
                            "message": "No Chat Found.!!",
                            "type": "Type Error",
                            "link": "search",
                        },
                    )
            else:
                return HttpResponse("Message Cannot be Empty.!")
        else:
            return HttpResponseRedirect(reverse("chat", args=(chat_id)))
    except KeyError:
        return render(
            request,
            "circle/error.html",
            context={"message": "Enter text.!!", "type": "Key Error", "link": "search"},
        )
    except ValueError:
        return render(
            request,
            "circle/error.html",
            context={
                "message": "Invalid Value to given field.!!",
                "type": "Value Error",
                "link": "search",
            },
        )
    except TypeError:
        return render(
            request,
            "circle/error.html",
            context={
                "message": "Incompatible DataType.!!",
                "type": "Type Error",
                "link": "search",
            },
        )


@login_required
def chat(request, chat_id):
    try:
        chat = Chat.objects.get(pk=chat_id)
        form = MessageForm()
        return render(request, "circle/chat.html", context={"chat": chat, "form": form})
    except Chat.DoesNotExist:
        return render(
            request,
            "circle/error.html",
            context={
                "message": "No Chat Found.!!",
                "type": "Type Error",
                "link": "chats",
            },
        )


@login_required
def chats(request):
    chats = Chat.objects.filter(
        Q(left=request.user.person) | Q(right=request.user.person)
    )
    return render(request, "circle/chats.html", context={"chats": chats})


@login_required
def update(request):
    user_id = request.user.id

    if request.POST:
        try:
            first = str(request.POST.get("first"))
        except KeyError:
            return render(
                request,
                "flights/error.html",
                context={"message": "Enter a First Name!!", "type": "Key Error!!"},
            )
        except ValueError:
            return render(
                request,
                "flights/error.html",
                context={
                    "message": "Invalid Value to given field!!",
                    "type": "Value Error!!",
                },
            )
        except TypeError:
            return render(
                request,
                "flights/error.html",
                context={
                    "message": "Incompatible DataType!!",
                    "type": "Type Error!!",
                },
            )

        try:
            last = str(request.POST.get("last"))
        except KeyError:
            return render(
                request,
                "flights/error.html",
                context={"message": "Enter a Last Name!!", "type": "Key Error!!"},
            )
        except ValueError:
            return render(
                request,
                "flights/error.html",
                context={
                    "message": "Invalid Value to given field!!",
                    "type": "Value Error!!",
                },
            )
        except TypeError:
            return render(
                request,
                "flights/error.html",
                context={
                    "message": "Incompatible DataType!!",
                    "type": "Type Error!!",
                },
            )

        try:
            email = str(request.POST.get("email"))
        except KeyError:
            return render(
                request,
                "flights/error.html",
                context={"message": "Enter a e-mail address!!", "type": "KeyError!!"},
            )
        except ValueError:
            return render(
                request,
                "flights/error.html",
                context={
                    "message": "Invalid Value to given field!!",
                    "type": "Value Error!!",
                },
            )
        except TypeError:
            return render(
                request,
                "flights/error.html",
                context={
                    "message": "Incompatible DataType!!",
                    "type": "Type Error!!",
                },
            )

        try:
            user = User.objects.get(pk=user_id)
            User.objects.update(first_name=first, last_name=last, email=email)
            user.save()
            return render(request, "circle/user.html", context={"user": user})
        except User.DoesNotExist:
            return render(
                request,
                "circle/error.html",
                context={
                    "message": "User Doesn't Exist!",
                    "type": "Value DoesNotExist.!!",
                    "link": "search",
                },
            )
    else:
        return HttpResponseRedirect(reverse("user", args=(user_id,)))


@login_required
def user(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
        return render(request, "circle/user.html", context={"user": user})
    except User.DoesNotExist:
        return render(
            request,
            "circle/error.html",
            context={
                "message": "User Doesn't Exist!!",
                "type": "Value DoesNotExist!!",
                "link": "users",
            },
        )


@login_required
def users(request):
    users = User.objects.all()
    return render(request, "circle/users.html", context={"users": users})


@login_required
def error(request):
    return render(
        request,
        "circle/error.html",
        context={
            "message": "Incompatible DataType.!!",
            "type": "Type Error",
            "link": "home",
        },
    )
