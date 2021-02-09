from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('article', views.article, name='article'),
    path('search', views.search, name='search'),
    path('user', views.user, name='user'),
    path('update', views.update, name='update'),
]
