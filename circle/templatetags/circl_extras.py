from django import template

from circle.models import Article, Person, Tag, Message, Chat

register = template.Library()

@register.filter()
def isDisplayed(person_id, article):
	try:
		person = Person.objects.get(pk=person_id)
		return article in person.display.all()
	except Person.DoesNotExist:
		return False