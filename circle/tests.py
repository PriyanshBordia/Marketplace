from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver

from .models import Article, Person, Message, Tag
from .views import addArticle, article, articles, home, addPerson, newArticle, newPerson, person, persons, friends, rented, wishlist, cart, result, search, user, users, update, message, error

# Create your tests here.

# class BrowserTest(StaticLiveServerTestCase):

# 	def setUp(self) -> None:
# 		super().setUp()

# 		self.browser = webdriver.Safari()


# class ModelsTestCase(TestCase):

# 	def setUp(self) -> None:

# 		# Base Class setUp
# 		super().setUp()

# 		a1 = Article.objects.create(title="Article 1", bio="")
# 		a1 = Article.objects.create(title="Article 2", bio="")
# 		a3 = Article.objects.create(title="Article 3", bio="")

# 	def test_is_valid_article(self):
# 		self.a1.is_valid_article()


class UrlsTestCase(TestCase):

	def __init__(self, methodName: str) -> None:
		super().__init__(methodName=methodName)
		self.view_functions_list = [addPerson,newArticle, addArticle]
	
	def test_url_home(self):
		url = reverse('home')
		self.assertEquals(resolve(url).func, home)
		
	def test_url_newPerson(self):
		url = reverse('newPerson')
		self.assertEquals(resolve(url).func, newPerson)

	def test_url_persons(self):
		url = reverse('persons')
		self.assertEquals(resolve(url).func, persons)
	
	def test_url_friends(self):
		url = reverse('friends')
		self.assertEquals(resolve(url).func, friends)

	def test_url_rented(self):
		url = reverse('rented')
		self.assertEquals(resolve(url).func, rented)

	def test_url_wishlist(self):
		url = reverse('wishlist')
		self.assertEquals(resolve(url).func, wishlist)

	def test_url_cart(self):
		url = reverse('cart')
		self.assertEquals(resolve(url).func, cart)

	def test_url_message(self):
		url = reverse('message')
		self.assertEquals(resolve(url).func, message)
	
	def test_url_users(self):
		url = reverse('users')
		self.assertEquals(resolve(url).func, users)
	
	def test_url_search(self):
		url = reverse('search')
		self.assertEquals(resolve(url).func, search)
	
	def test_url_result(self):
		url = reverse('result')
		self.assertEquals(resolve(url).func, result)
	
	def test_url_update(self):
		url = reverse('update')
		self.assertEquals(resolve(url).func, update)

	def test_url_error(self):
		url = reverse('error')
		self.assertEquals(resolve(url).func, error)

	def test_url_person(self):
		url = reverse('person', args=[1])
		self.assertEqual(resolve(url).func, person)

	def test_url_article(self):
		url = reverse('article', args=[1])
		self.assertEqual(resolve(url).func, article)

	def test_url_user(self):
		url = reverse('user', args=[1])
		self.assertEquals(resolve(url).func, user)


class ViewsTestCase(TestCase):

	def __init__(self, methodName: str) -> None:
		super().__init__(methodName=methodName)

	def setUp(self) -> None:
		super().setUp()
		self.response = self.client.get(reverse('home'))

	def test_view_status_code(self):
		self.assertEquals(self.response.status_code, 200)

	def test_view_template_used(self):
		self.assertTemplateUsed(self.response, "circle/home.html")
