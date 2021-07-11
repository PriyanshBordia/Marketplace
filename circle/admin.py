from django.contrib import admin

from .models import Article, Person, Message, Tag, Chat

# Register your models here.

admin.site.register(Tag)
admin.site.register(Article)
admin.site.register(Person)
admin.site.register(Message)
admin.site.register(Chat)
