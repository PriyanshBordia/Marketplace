from django.test import TestCase
from django.urls import reverse, resolve
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth.models import User
from django.core.management import call_command

from .models import Article, Person, Message, Tag, Chat
from .views import home, newArticle, addArticle, article, articles, newPerson, addPerson, person, persons, friends, rented, wishlist, cart, result, search, user, users, update, message, error

# Create your tests here.


# class BrowserTest(StaticLiveServerTestCase):

# 	def setUp(self) -> None:
# 		super().setUp()

# 		self.browser = webdriver.Safari()

# Test for models
# class ModelsTestCase(TestCase):

# 	def __init__(self, methodName: str) -> None:
# 		super().__init__(methodName=methodName)

# 	def setUp(self) -> None:

# 		# Base Class setUp
# 		super().setUp()

# 		a1 = Article.objects.create(title="Article 1", bio="a1 bio")
# 		a1 = Article.objects.create(title="Article 2", bio="a2 bio")
# 		a3 = Article.objects.create(title="Article 3", bio="a bio")

		
# 	def test_is_valid_article(self):
# 		self.a1.is_valid_article()

# Test for urls
class UrlsTestCase(TestCase):

	def __init__(self, methodName: str) -> None:
		super().__init__(methodName=methodName)
		self.view_functions_list = [addPerson,addArticle]
	
	def setUp(self) -> None:
		return super().setUp()

	def test_url_home(self):
		url = reverse('home')
		self.assertEquals(resolve(url).func, home)

	def test_url_newPerson(self):
		url = reverse('newPerson')
		self.assertEquals(resolve(url).func, newPerson)
	
	def test_url_addPerson(self):
		url = reverse('addPerson')
		self.assertEquals(resolve(url).func, addPerson)

	def test_url_persons(self):
		url = reverse('persons')
		self.assertEquals(resolve(url).func, persons)

	def test_url_newArticle(self):
		url = reverse('newArticle')
		self.assertEquals(resolve(url).func, newArticle)
	
	def test_url_addArticle(self):
		url = reverse('addArticle')
		self.assertEquals(resolve(url).func, addArticle)

	def test_url_articles(self):
		url = reverse('articles')
		self.assertEquals(resolve(url).func, articles)

	def test_url_persons(self):
		url = reverse('persons')
		self.assertEquals(resolve(url).func, persons)
	
	def test_url_friends(self):
		url = reverse('friends')
		self.assertEquals(resolve(url).func, friends)

	def test_url_search(self):
		url = reverse('search')
		self.assertEquals(resolve(url).func, search)

	def test_url_result(self):
		url = reverse('result')
		self.assertEquals(resolve(url).func, result)

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

# Test for views
class ViewsTestCase(TestCase):

	def __init__(self, methodName: str) -> None:
		super().__init__(methodName=methodName)

	def setUp(self) -> None:
		super().setUp()
		
		user = User.objects.create_user('test', 'test@mail.co', 'test')
		self.client.login(username='test', password='test')

		t1 = Tag.objects.create(name="test-tag", domain="testing", description="a tag for testing.!", slug="test-tag")

		a1 = Article.objects.create(title="Test A1", description="Test A1 bio", image="test", price=990, slug="test-slug")
		a1.tags.add(t1)

		Person.objects.create(user=user, username="test", profile="test", bio="Test A1 bio", first="test", last="test", age=19, sex='X', email="test@mail.io", ph_no=9876543210, slug="test-slug")
		

	def test_view_status_code_home(self):
		self.response = self.client.get(reverse('home'))
		self.assertEquals(self.response.status_code, 200)

	def test_view_template_used_home(self):
		self.response = self.client.get(reverse('home'))
		self.assertTemplateUsed(self.response, "circle/home.html")

	def test_view_status_code_newArticle(self):
		self.response = self.client.get(reverse('newArticle'))
		self.assertEquals(self.response.status_code, 200)

	def test_view_template_used_newArticle(self):
		self.response = self.client.get(reverse('newArticle'))
		self.assertTemplateUsed(self.response, "circle/newArticle.html")

	def test_view_status_code_article(self):
		self.response = self.client.get(reverse('article', args=(1,)))
		self.assertEquals(self.response.status_code, 200)

	def test_view_template_used_article(self):
		self.response = self.client.get(reverse('article', args=(1,)))
		self.assertTemplateUsed(self.response, "circle/article.html")

	def test_view_status_code_articles(self):
		self.response = self.client.get(reverse('articles'))
		self.assertEquals(self.response.status_code, 200)

	def test_view_template_used_articles(self):
		self.response = self.client.get(reverse('articles'))
		self.assertTemplateUsed(self.response, "circle/articles.html")

	def test_view_status_code_person(self):
		self.response = self.client.get(reverse('person', args=(1,)))
		self.assertEquals(self.response.status_code, 200)

	def test_view_template_used_person(self):
		self.response = self.client.get(reverse('person', args=(1,)))
		self.assertTemplateUsed(self.response, "circle/person.html")

	def test_view_status_code_persons(self):
		self.response = self.client.get(reverse('persons'))
		self.assertEquals(self.response.status_code, 200)

	def test_view_template_used_persons(self):
		self.response = self.client.get(reverse('persons'))
		self.assertTemplateUsed(self.response, "circle/persons.html")

	def test_view_status_code_friends(self):
		self.response = self.client.get(reverse('friends'))
		self.assertEquals(self.response.status_code, 200)

	def test_view_template_used_friends(self):
		self.response = self.client.get(reverse('friends'))
		self.assertTemplateUsed(self.response, "circle/friends.html")
	
	def test_view_status_code_newPerson(self):
		self.response = self.client.get(reverse('newPerson'))
		self.assertEquals(self.response.status_code, 200)

	def test_view_template_used_newPerson(self):
		self.response = self.client.get(reverse('newPerson'))
		self.assertTemplateUsed(self.response, "circle/newPerson.html")

	def test_view_status_code_newArticle(self):
		self.response = self.client.get(reverse('newArticle'))
		self.assertEquals(self.response.status_code, 200)

	def test_view_template_used_newArticle(self):
		self.response = self.client.get(reverse('newArticle'))
		self.assertTemplateUsed(self.response, "circle/newArticle.html")


# Test for the templates
class TemplatesTestCase(TestCase):
    def test_validate_templates(self):
        call_command("validate_templates")
