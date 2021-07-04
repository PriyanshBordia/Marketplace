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
    path('search', views.search, name='search'),
    path('result', views.result, name='result'),
    path('user', views.user, name='user'),
    path('update', views.update, name='update'),
]
