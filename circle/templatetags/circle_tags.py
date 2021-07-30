from django import template

from termcolor import cprint

from circle.models import Article, Person, Tag, Message, Chat

register = template.Library()

@register.filter(name='isSender')
def isSender(value, arg):
	try:
		person = Person.objects.get(username=value)
		chat_id = arg[0]
		chat = Chat.objects.get(pk=chat_id)
	except Chat.DoesNotExist:
		cprint("Chat does not exist", 'red')
		return False


@register.filter(name='isDisplayed')
def isDisplayed(value, arg):
	try:
		person_id = int(arg[0])
		return Person.objects.filter(id=person_id, display__pk=value.id).exists()
	except Person.DoesNotExist:
		return False


@register.filter(name='isWishlisted')
def isWishlisted(value, arg):
	try:
		person_id = int(arg[0])
		return Person.objects.filter(id=person_id, bookmarked__pk=value.id).exists()
	except Person.DoesNotExist:
		return False


@register.filter(name='isRented')
def isRented(value, arg):
	try:
		person_id = int(arg[0])
		return Person.objects.filter(id=person_id, rented__pk=value.id).exists()
	except Person.DoesNotExist:
		return False


@register.filter(name='isPurchased')
def isPurchased(value, arg):
	try:
		person_id = int(arg[0])
		return Person.objects.filter(id=person_id, purchased__pk=value.id).exists()
	except Person.DoesNotExist:
		return False
