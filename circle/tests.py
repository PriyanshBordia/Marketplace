from django.test import TestCase, Client, client
from django.urls import reverse, resolve

from .models import Article, Person, Message, Tag
from .views import addArticle, article, articles, home, addPerson, newArticle, person, persons, result, search, user, users, update, message

# Create your tests here.

class ModelsTestCase(TestCase):

	def setUp(self) -> None:

		# Base Class setUp
		super().setUp()

		a1 = Article.objects.create(title="Article 1", bio="")
		a1 = Article.objects.create(title="Article 2", bio="")
		a3 = Article.objects.create(title="Article 3", bio="")


	def test_is_valid_article(self):
		a1.is_valid_article()


class UrlsTestCase(TestCase):

	def __init__(self, methodName: str) -> None:
		super().__init__(methodName=methodName)
		self.view_functions_list = [home, addPerson, persons, newArticle, addArticle, articles, user, users, search, result, update, message]
		self.params_view_functions_list = [person, article]
	
	def test_urls(self):
		for view in self.view_functions_list:
			url = reverse(view)
			self.assertEquals(resolve(url).func, view)

	def test_urls_parmas(self):
		for view in self.params_view_functions_list:
			url = reverse(view, args=[1])
			self.assertEqual(resolve(url).func, view)


class ViewsTestCase(TestCase):

	def __init__(self, methodName: str) -> None:
		super().__init__(methodName=methodName)

	def setUp(self) -> None:
		super().setUp()
		self.client = Client()
		self.response = self.client.get(reverse('home'))

	# def view_response(self):
		# pass

	def test_view_status_code(self):
		self.assertEquals(self.response.status_code, 200)

	def test_view_template_used(self):
		self.assertTemplateUsed(self.response, "circle/home.html")
