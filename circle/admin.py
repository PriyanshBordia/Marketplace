from django.contrib import admin

from .models import Article, Person, Message, Tag, Chat

# Register your models here.

class TagAdmin(admin.ModelAdmin):
	pass


class ArticleAdmin(admin.ModelAdmin):
	pass


class PersonAdmin(admin.ModelAdmin):
	pass


class MessageAdmin(admin.ModelAdmin):
	pass


class ChatAdmin(admin.ModelAdmin):
	pass


admin.site.register(Tag, TagAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Chat, ChatAdmin)
