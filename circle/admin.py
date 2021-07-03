from django.contrib import admin

from .models import Article, Person, Message, Tag
# Register your models here.


admin.site.register(Article)
admin.site.register(Person)
admin.site.register(Message)
admin.site.register(Tag)