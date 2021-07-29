from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
   	path('newPerson', views.newPerson, name='newPerson'),
   	path('addPerson', views.addPerson, name='addPerson'),
    path('person/<int:person_id>', views.person, name='person'),
    path('persons', views.persons, name='persons'),
   	path('edit/<int:id>/<str:type>', views.edit, name='edit'),
    path('newArticle', views.newArticle, name='newArticle'),
    path('addArticle', views.addArticle, name='addArticle'),
    path('article/<int:article_id>', views.article, name='article'),
    path('articles', views.articles, name='articles'),
   	path('update', views.update, name='update'),
    path('addFriend/<int:person_id>', views.addFriend, name='addFriend'),
    path('friends', views.friends, name='friends'),
    path('search', views.search, name='search'),
    path('result', views.result, name='result'),
    path('display', views.display, name='display'),
    path('wishlist/<int:article_id>', views.wishlist, name='wishlist'),
   	path('rent/<int:article_id>', views.rent, name='rent'),
    path('cart/<int:article_id>', views.cart, name='cart'),
    path('buy/<int:article_id>', views.buy, name='buy'),
   	path('purchased', views.purchased, name='purchased'),
   	path('sold', views.sold, name='sold'),
    path('wishlisted', views.wishlisted, name='wishlisted'),
   	path('rented', views.rented, name='rented'),
    path('carted', views.carted, name='carted'),
   	path('remove/<int:id>/<str:type>', views.remove, name='remove'),
    path('addMessage/<int:chat_id>', views.addMessage, name='addMessage'),
    path('chat/<int:chat_id>', views.chat, name='chat'),
    path('chats', views.chats, name='chats'),
   	path('user/<int:user_id>', views.user, name='user'),
    path('users', views.users, name='users'),
	path('error', views.error, name='error'),
   	# path('verification', views.verification, name='verification'),
]
