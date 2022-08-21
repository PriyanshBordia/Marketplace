from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from django.core.management import call_command

from .models import Article, Person, Message, Tag, Chat
from . import views


# Create your tests here.


# Test for models
class ModelsTestCase(TestCase):

	def __init__(self, methodName: str) -> None:
		super().__init__(methodName=methodName)

	def setUp(self) -> None:

		# Base Class setUp
		super().setUp()

		a1 = Article.objects.create(title="Article 1", description="a1 description", image="test.png", price=990)
		a2 = Article.objects.create(title="Article 2", description="a2 description", image="test.png", price=990)
		a3 = Article.objects.create(title="Article 3", description="a3 description", image="test.png", price=890)
		
# 	def test_is_valid_article(self):
# 		a1.is_valid_article()
# 		a2.is_valid_article()
# 		a3.is_valid_article()


# Test for urls
class UrlsTestCase(TestCase):

	def __init__(self, methodName: str) -> None:
		super().__init__(methodName=methodName)

	def test_url_home(self):
		url = reverse('home')
		self.assertEquals(resolve(url).func, views.home)

	def test_url_newPerson(self):
		url = reverse('newPerson')
		self.assertEquals(resolve(url).func, views.newPerson)
	
	def test_url_addPerson(self):
		url = reverse('addPerson')
		self.assertEquals(resolve(url).func, views.addPerson)

	def test_url_person(self):
		url = reverse('person', args=[1])
		self.assertEqual(resolve(url).func, views.person)

	def test_url_persons(self):
		url = reverse('persons')
		self.assertEquals(resolve(url).func, views.persons)

	def test_url_newArticle(self):
		url = reverse('newArticle')
		self.assertEquals(resolve(url).func, views.newArticle)
	
	def test_url_addArticle(self):
		url = reverse('addArticle')
		self.assertEquals(resolve(url).func, views.addArticle)

	def test_url_article(self):
		url = reverse('article', args=[1])
		self.assertEqual(resolve(url).func, views.article)
		
	def test_url_articles(self):
		url = reverse('articles')
		self.assertEquals(resolve(url).func, views.articles)
	
	def test_url_edit(self):
		url = reverse('edit', args=[1, 'test'])
		self.assertEquals(resolve(url).func, views.edit)
	
	def test_url_addTag(self):
		url = reverse('addTag',)
		self.assertEquals(resolve(url).func, views.addTag)
	
	def test_url_tag(self):
		url = reverse('tag', args=[1])
		self.assertEquals(resolve(url).func, views.tag)
	
	def test_url_tags(self):
		url = reverse('tags',)
		self.assertEquals(resolve(url).func, views.tags)

	def test_url_addFriend(self):
		url = reverse('addFriend', args=[1])
		self.assertEquals(resolve(url).func, views.addFriend)

	def test_url_friends(self):
		url = reverse('friends')
		self.assertEquals(resolve(url).func, views.friends)

	def test_url_search(self):
		url = reverse('search', args=['test-type'])
		self.assertEquals(resolve(url).func, views.search)

	def test_url_result(self):
		url = reverse('result', args=['test-type'])
		self.assertEquals(resolve(url).func, views.result)
	
	def test_url_display(self):
		url = reverse('display')
		self.assertEquals(resolve(url).func, views.display)

	def test_url_wishlist(self):
		url = reverse('wishlist', args=[1,])
		self.assertEquals(resolve(url).func, views.wishlist)

	def test_url_rent(self):
		url = reverse('rent', args=[1,])
		self.assertEquals(resolve(url).func, views.rent)
	
	def test_url_retreat(self):
		url = reverse('retreat', args=[1])
		self.assertEquals(resolve(url).func, views.retreat)

	def test_url_cart(self):
		url = reverse('cart', args=[1, ])
		self.assertEquals(resolve(url).func, views.cart)
	
	def test_url_buy(self):
		url = reverse('buy', args=[1, ])
		self.assertEquals(resolve(url).func, views.buy)

	def test_url_purchased(self):
		url = reverse('purchased')
		self.assertEquals(resolve(url).func, views.purchased)
	
	def test_url_sold(self):
		url = reverse('sold')
		self.assertEquals(resolve(url).func, views.sold)

	def test_url_wishlisted(self):
		url = reverse('wishlisted')
		self.assertEquals(resolve(url).func, views.wishlisted)

	def test_url_rented(self):
		url = reverse('rented')
		self.assertEquals(resolve(url).func, views.rented)

	def test_url_carted(self):
		url = reverse('carted')
		self.assertEquals(resolve(url).func, views.carted)

	def test_url_retreated(self):
		url = reverse('retreated')
		self.assertEquals(resolve(url).func, views.retreated)

	def test_url_remove(self):
		url = reverse('remove', args=[1, 'article'])
		self.assertEquals(resolve(url).func, views.remove)

	def test_url_addMessage(self):
		url = reverse('addMessage', args=[1])
		self.assertEquals(resolve(url).func, views.addMessage)
	
	def test_url_chat(self):
		url = reverse('chat', args=[1])
		self.assertEquals(resolve(url).func, views.chat)
	
	def test_url_chats(self):
		url = reverse('chats')
		self.assertEquals(resolve(url).func, views.chats)

	def test_url_update(self):
		url = reverse('update')
		self.assertEquals(resolve(url).func, views.update)

	def test_url_user(self):
		url = reverse('user', args=[1])
		self.assertEquals(resolve(url).func, views.user)

	def test_url_users(self):
		url = reverse('users')
		self.assertEquals(resolve(url).func, views.users)

	def test_url_error(self):
		url = reverse('error')
		self.assertEquals(resolve(url).func, views.error)	


# Test for views
class ViewsTestCase(TestCase):

	def __init__(self, methodName: str) -> None:
		super().__init__(methodName=methodName)

	def setUp(self) -> None:
		super().setUp()
		
		user = User.objects.create_user('test', 'test@mail.co', 'test')
		self.client.login(username='test', password='test')
		self.user_id = user.id

		t1 = Tag.objects.create(name="test-tag", domain="testing", description="a tag for testing.!")
		self.tag_id = t1.id

		a1 = Article.objects.create(title="Test A1", description="Test A1 bio", image="test.png", price=990)
		self.article_id = a1.id
		a1.tags.add(t1)
		a1.save()

		p1 = Person.objects.create(user=user, username="test", profile="test", bio="Test A1 bio", first="test", last="test", age=19, sex='X', email="test@mail.io", ph_no=9876543210, slug="test-slug")
		self.person_id = p1.id
		p1.display.add(a1)
		p1.save()

		c1 = Chat.objects.create(left=p1, right=p1)
		self.chat_id = c1.id

	def test_view_status_code_login(self):
		self.response = self.client.get(reverse('login'))
		self.assertEquals(self.response.status_code, 200)

	def test_view_template_used_login(self):
		self.response = self.client.get(reverse('login'))
		self.assertTemplateUsed(self.response, "registration/login.html")

	def test_view_template_used_signup(self):
		self.response = self.client.get(reverse('signup'))
		self.assertTemplateUsed(self.response, "registration/signup.html")

	def test_view_status_code_signup(self):
		self.response = self.client.get(reverse('signup'))
		self.assertEquals(self.response.status_code, 200)


	def test_view_status_code_home(self):
		self.response = self.client.get(reverse('home'))
		self.assertEquals(self.response.status_code, 200)

	def test_view_template_used_home(self):
		self.response = self.client.get(reverse('home'))
		self.assertTemplateUsed(self.response, "circle/home.html")
	
	def test_view_status_code_addPerson(self):
		self.response = self.client.get(reverse('addPerson'))
		self.assertEquals(self.response.status_code, 200)
		self.response = self.client.post(reverse('addPerson'), {'profile': 'test.png', 'bio': 'Test A1 bio', 'first': 'test', 'last': 'test', 'age': 19, 'sex': 'X', 'email': 'test@mail.io', 'ph_no': 9876543210})
		self.assertEquals(self.response.status_code, 200)

	def test_view_template_used_addPerson(self):
		self.response = self.client.get(reverse('addPerson'))
		self.assertTemplateUsed(self.response, "circle/person.html")
		# self.response = self.client.post(reverse('addPerson'), {'profile':'test.png', 'bio':'Test A1 bio', 'first': 'test', 'last': 'test', 'age': 19, 'sex':'X', 'email':'test@mail.io', 'ph_no': 9876543210})

	def test_view_status_code_newPerson(self):
		self.response = self.client.get(reverse('newPerson'))
		self.assertEquals(self.response.status_code, 200)

	def test_view_template_used_newPerson(self):
		self.response = self.client.get(reverse('newPerson'))
		self.assertTemplateUsed(self.response, "circle/newPerson.html")

	def test_view_status_code_person(self):
		self.response = self.client.get(reverse('person', args=(self.person_id,)))
		self.assertEquals(self.response.status_code, 200)

	def test_view_template_used_person(self):
		self.response = self.client.get(reverse('person', args=(self.person_id,)))
		self.assertTemplateUsed(self.response, "circle/person.html")

	def test_view_status_code_persons(self):
		self.response = self.client.get(reverse('persons'))
		self.assertEquals(self.response.status_code, 200)

	def test_view_template_used_persons(self):
		self.response = self.client.get(reverse('persons'))
		self.assertTemplateUsed(self.response, "circle/persons.html")

	def test_view_status_code_addArticle(self):
		self.response = self.client.get(reverse('addArticle'))
		self.assertEquals(self.response.status_code, 200)
		self.response = self.client.post(reverse('addArticle'), {'title':'Test A1', 'description':'Test A1 bio', 'image':'test.png', 'price':990})
		self.assertEquals(self.response.status_code, 200)

	def test_view_template_used_addArticle(self):
		self.response = self.client.get(reverse('addArticle'))
		self.assertTemplateUsed(self.response, "circle/article.html")
		# self.response = self.client.post(reverse('addArticle'), {'title':'Test A1', 'description':'Test A1 bio', 'image':'test.png', 'price':990})

	def test_view_status_code_newArticle(self):
		self.response = self.client.get(reverse('newArticle'))
		self.assertEquals(self.response.status_code, 200)

	def test_view_template_used_newArticle(self):
		self.response = self.client.get(reverse('newArticle'))
		self.assertTemplateUsed(self.response, "circle/newArticle.html")

	def test_view_status_code_article(self):
		self.response = self.client.get(reverse('article', args=(self.article_id,)))
		self.assertEquals(self.response.status_code, 200)

	def test_view_template_used_article(self):
		self.response = self.client.get(reverse('article', args=(self.article_id,)))
		self.assertTemplateUsed(self.response, "circle/article.html")

	def test_view_status_code_articles(self):
		self.response = self.client.get(reverse('articles'))
		self.assertEquals(self.response.status_code, 200)

	def test_view_template_used_articles(self):
		self.response = self.client.get(reverse('articles'))
		self.assertTemplateUsed(self.response, "circle/articles.html")
	
	def test_view_status_code_tag(self):
		self.response = self.client.get(reverse('tag', args=(self.tag_id, )))
		self.assertEquals(self.response.status_code, 200)

	def test_view_template_used_tag(self):
		self.response = self.client.get(reverse('tag', args=(self.tag_id, )))
		self.assertTemplateUsed(self.response, "circle/tag.html")

	def test_view_status_code_tags(self):
		self.response = self.client.get(reverse('tags'))
		self.assertEquals(self.response.status_code, 200)

	def test_view_template_used_tags(self):
		self.response = self.client.get(reverse('tags'))
		self.assertTemplateUsed(self.response, "circle/tags.html")

	# def test_view_status_code_addFriend(self):
	# 	self.response = self.client.get(reverse('addFriend', args=(self.person_id, )))
	# 	self.assertEquals(self.response.status_code, 302)

	# def test_view_template_used_addFriend(self):
	# 	self.response = self.client.get(reverse('addFriend', args=(self.person_id, )))
	# 	self.assertTemplateUsed(self.response, "circle/person.html")

	def test_view_status_code_friends(self):
		self.response = self.client.get(reverse('friends'))
		self.assertEquals(self.response.status_code, 200)

	def test_view_template_used_friends(self):
		self.response = self.client.get(reverse('friends'))
		self.assertTemplateUsed(self.response, "circle/friends.html")

	def test_view_status_code_search(self):
		self.response = self.client.get(reverse('search', args=('person', )))
		self.assertEquals(self.response.status_code, 200)

	def test_view_template_used_search(self):
		self.response = self.client.get(reverse('search', args=('person', )))
		self.assertTemplateUsed(self.response, "circle/search.html")
		
	def test_view_status_code_result(self):
		self.response = self.client.post(reverse('result', args=('article', )), {"search": "Test"})
		self.assertEquals(self.response.status_code, 200)

	def test_view_template_used_result(self):
		self.response = self.client.post(reverse('result', args=('article', )), {"search": "Test"})
		self.assertTemplateUsed(self.response, "circle/result.html")
	
	def test_view_status_code_display(self):
		self.response = self.client.get(reverse('display'))
		self.assertEquals(self.response.status_code, 200)

	def test_view_template_used_display(self):
		self.response = self.client.get(reverse('display'))
		self.assertTemplateUsed(self.response, "circle/display.html")
	
	def test_view_status_code_wishlist(self):
		self.response = self.client.get(reverse('wishlist', args=(self.article_id, )))
		self.assertEquals(self.response.status_code, 302)

	# def test_view_template_used_wishlist(self):
	# 	self.response = self.client.get(reverse('wishlist', args=(self.article_id, )))
	# 	self.assertTemplateUsed(self.response, "circle/wishlist.html")
	
	def test_view_status_code_rent(self):
		self.response = self.client.get(reverse('rent', args=(self.article_id, )))
		self.assertEquals(self.response.status_code, 302)

	# def test_view_template_used_rent(self):
	# 	self.response = self.client.get(reverse('rent', args=(self.article_id, )))
	# 	self.assertTemplateUsed(self.response, "circle/rent.html")
	
	def test_view_status_code_retreat(self):
		self.response = self.client.get(reverse('retreat', args=(self.article_id, )))
		self.assertEquals(self.response.status_code, 302)

	# def test_view_template_used_retreat(self):
	# 	self.response = self.client.get(reverse('retreat', args=(self.article_id, )))
	# 	self.assertTemplateUsed(self.response, "circle/retreat.html")

	def test_view_status_code_cart(self):
		self.response = self.client.get(reverse('cart', args=(self.article_id, )))
		self.assertEquals(self.response.status_code, 302)

	# def test_view_template_used_cart(self):
	# 	self.response = self.client.get(reverse('cart', args=(self.article_id, )))
	# 	self.assertTemplateUsed(self.response, "circle/cart.html")

	def test_view_status_code_buy(self):
		self.response = self.client.get(reverse('buy', args=(self.article_id, )))
		self.assertEquals(self.response.status_code, 302)

	# def test_view_template_used_buy(self):
	# 	self.response = self.client.get(reverse('buy', args=(self.article_id, )))
	# 	self.assertTemplateUsed(self.response, "circle/purchased.html")
	
	def test_view_status_code_purchased(self):
		self.response = self.client.get(reverse('purchased'))
		self.assertEquals(self.response.status_code, 200)

	def test_view_template_used_purchased(self):
		self.response = self.client.get(reverse('purchased'))
		self.assertTemplateUsed(self.response, "circle/purchased.html")

	def test_view_status_code_sold(self):
		self.response = self.client.get(reverse('sold'))
		self.assertEquals(self.response.status_code, 200)

	def test_view_template_used_sold(self):
		self.response = self.client.get(reverse('sold'))
		self.assertTemplateUsed(self.response, "circle/sold.html")

	def test_view_status_code_wishlisted(self):
		self.response = self.client.get(reverse('wishlisted'))
		self.assertEquals(self.response.status_code, 200)

	def test_view_template_used_wishlisted(self):
		self.response = self.client.get(reverse('wishlisted'))
		self.assertTemplateUsed(self.response, "circle/wishlist.html")

	def test_view_status_code_rented(self):
		self.response = self.client.get(reverse('rented'))
		self.assertEquals(self.response.status_code, 200)

	def test_view_template_used_rented(self):
		self.response = self.client.get(reverse('rented'))
		self.assertTemplateUsed(self.response, "circle/rent.html")
	
	def test_view_status_code_carted(self):
		self.response = self.client.get(reverse('carted'))
		self.assertEquals(self.response.status_code, 200)

	def test_view_template_used_carted(self):
		self.response = self.client.get(reverse('carted'))
		self.assertTemplateUsed(self.response, "circle/cart.html")
	
	def test_view_template_used_retreated(self):
		self.response = self.client.get(reverse('retreated'))
		self.assertTemplateUsed(self.response, "circle/retreat.html")
	
	def test_view_status_code_retreated(self):
		self.response = self.client.get(reverse('retreated'))
		self.assertEquals(self.response.status_code, 200)

	def test_view_status_code_remove(self):
		self.response = self.client.get(reverse('remove', args=(self.person_id, 'person')))
		self.assertEquals(self.response.status_code, 302)

	# def test_view_template_used_remove(self):
	# 	self.response = self.client.get(reverse('remove', args=(self.person_id, 'person')))
	# 	self.assertTemplateUsed(self.response, "circle/remove.html") 
 
	# def test_view_status_code_addMessage(self):
	# 	self.response = self.client.get(reverse('addMessage', args=(self.msg_id, )))
	# 	self.assertEquals(self.response.status_code, 200)

	# def test_view_template_used_addMessage(self):
	# 	self.response = self.client.get(reverse('addMessage', args=(self.msg_id, )))
	# 	self.assertTemplateUsed(self.response, "circle/chat.html")

	def test_view_status_code_chat(self):
		self.response = self.client.get(reverse('chat', args=(self.chat_id, )))
		self.assertEquals(self.response.status_code, 200)

	def test_view_template_used_chat(self):
		self.response = self.client.get(reverse('chat', args=(self.chat_id, )))
		self.assertTemplateUsed(self.response, "circle/chat.html")

	def test_view_status_code_chats(self):
		self.response = self.client.get(reverse('chats'))
		self.assertEquals(self.response.status_code, 200)

	def test_view_template_used_chats(self):
		self.response = self.client.get(reverse('chats'))
		self.assertTemplateUsed(self.response, "circle/chats.html")

	def test_view_status_code_update(self):
		self.response = self.client.post(reverse('update'), {"first": "first", "last": "last", "email": "mail@mail.co"})
		self.assertEquals(self.response.status_code, 200)

	def test_view_template_used_update(self):
		self.response = self.client.post(reverse('update'), {"first": "first", "last": "last", "email": "mail@mail.co"})
		self.assertTemplateUsed(self.response, "circle/user.html")

	def test_view_status_code_user(self):
		self.response = self.client.get(reverse('user', args=(self.user_id, )))
		self.assertEquals(self.response.status_code, 200)

	def test_view_template_used_user(self):
		self.response = self.client.get(reverse('user', args=(self.user_id, )))
		self.assertTemplateUsed(self.response, "circle/user.html")

	def test_view_status_code_users(self):
		self.response = self.client.get(reverse('users'))
		self.assertEquals(self.response.status_code, 200)

	def test_view_template_used_users(self):
		self.response = self.client.get(reverse('users'))
		self.assertTemplateUsed(self.response, "circle/users.html")

	def test_view_status_code_error(self):
		self.response = self.client.get(reverse('error'))
		self.assertEquals(self.response.status_code, 200)

	def test_view_template_used_error(self):
		self.response = self.client.get(reverse('error'))
		self.assertTemplateUsed(self.response, "circle/error.html")

	def test_view_status_code_logout(self):
		self.response = self.client.get(reverse('logout'))
		self.assertEquals(self.response.status_code, 302)

	# def test_view_template_used_logout(self):
	# 	self.response = self.client.get(reverse('logout'))
	# 	self.assertTemplateUsed(self.response, "circle/home.html")
		

# Test for the templates
class TemplatesTestCase(TestCase):
    def test_validate_templates(self):
        call_command("validate_templates")
