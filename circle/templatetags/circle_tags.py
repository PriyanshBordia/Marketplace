from django import template

from django.db.models import Q

from circle.models import Article, Person, Tag, Message, Chat


register = template.Library()


@register.filter(name='get_chat_id')
def chatId(value, arg):
	try:
		person_id = int(arg)
		person = Person.objects.get(pk=person_id)
		friend = value
		return Chat.objects.filter(Q(left=person, right=friend) | Q(left=friend, right=person)).first().id
	except Person.DoesNotExist:
		return  False
	except Chat.DoesNotExist:
		return False


@register.filter(name='isTag')
def isTag(value, arg):
	try:
		person_id = int(arg)
		return Person.objects.filter(id=person_id, tags__pk=value.id).exists()
	except Person.DoesNotExist:
		return False 


@register.filter(name='isFriend')
def isFriend(value, arg):
	try:
		person_id = int(arg)
		return Person.objects.filter(id=person_id, friends__pk=value.id).exists()
	except Person.DoesNotExist:
		return False


@register.filter(name='isDisplayed')
def isDisplayed(value, arg):
	try:
		person_id = int(arg)
		return Person.objects.filter(id=person_id, display__pk=value.id).exists()
	except Person.DoesNotExist:
		return False


@register.filter(name='isPurchased')
def isPurchased(value, arg):
	try:
		person_id = int(arg)
		return Person.objects.filter(id=person_id, purchased__pk=value.id).exists()
	except Person.DoesNotExist:
		return False


@register.filter(name='isWishlisted')
def isWishlisted(value, arg):
	try:
		person_id = int(arg)
		return Person.objects.filter(id=person_id, bookmarked__pk=value.id).exists()
	except Person.DoesNotExist:
		return False


@register.filter(name='isRented')
def isRented(value, arg):
	try:
		person_id = int(arg)
		return Person.objects.filter(id=person_id, rented__pk=value.id).exists()
	except Person.DoesNotExist:
		return False


@register.filter(name='isRetreated')
def isRetreated(value, arg):
	try:
		person_id = int(arg)
		return Person.objects.filter(id=person_id, retreated__pk=value.id).exists()
	except Person.DoesNotExist:
		return False


@register.filter(name='isSold')
def isSold(value, arg):
	try:
		person_id = int(arg)
		return Person.objects.filter(id=person_id, sold__pk=value.id).exists()
	except Person.DoesNotExist:
		return False
