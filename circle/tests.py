from django.test import TestCase
from django.urls import reverse, resolve

from .views import addArticle, article, articles, home, addPerson, newArticle, person, persons, result, search, user, users, update, message

# Create your tests here.

class TestViews(TestCase):
	
	# def __init__(self):
	view_functions_list = [home, addPerson, persons, newArticle, addArticle, articles, user, users, search, result, update, message]
	params_view_functions_list = [person, article]
	
	def test_urls(self):
		for view in TestViews.view_functions_list:
			url = reverse(view)
			self.assertEquals(resolve(url).func, view)


class TestModels(TestCase):

	def test(self):
		assert 1 == 1
