from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
   	path('addPerson', views.addPerson, name='addPerson'),
    path('person<int:person_id>', views.person, name='person'),
    path('persons', views.persons, name='persons'),
    path('newArticle', views.newArticle, name='newArticle'),
    path('addArticle', views.addArticle, name='addArticle'),
    path('article/<int:article_id>', views.article, name='article'),
    path('articles', views.articles, name='articles'),
  	path('update', views.update, name='update'),
    path('message', views.message, name='message'),
    path('search', views.search, name='search'),
    path('result', views.result, name='result'),
   	path('rent/<int:article_id>', views.rent, name='rent'),
    path('bookmark/<int:article_id>', views.bookmark, name='bookmark'),
    path('buy/<int:article_id>', views.buy, name='buy'),
   	path('rented', views.rented, name='rented'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('cart', views.cart, name='cart'),
    path('chat/<int:chat_id>', views.chat, name='chat'),
    path('chats', views.chats, name='chats'),
   	path('user', views.user, name='user'),
    path('users', views.users, name='users'),
    path('friends', views.friends, name='friends'),
	path('error', views.error, name='error'),
   	# path('rent/<int:article_id>', views.rent, name='rent'),
   	# path('bookmark/<int:article_id>', views.bookmark, name='bookmark'),
]
