from django import forms
from django.contrib.auth.models import User

from .models import Article, Person, Tag, Message, Chat

class UserForm(forms.ModelForm):

	class Meta:
		model = User
		fields = '__all__'


class ArticleForm(forms.ModelForm):

	class Meta:
		model = Article
		fields = ('title', 'description', 'image', 'price')


class PersonForm(forms.ModelForm):

	class Meta:
		model = Person
		fields = ('first', 'last', 'bio', 'profile', 'age', 'sex', 'email', 'ph_no', 'allowsMessage')


class MessageForm(forms.ModelForm):

	class Meta:
		model = Message
		fields = ('text', )


class ChatForm(forms.ModelForm):

	class Meta:
		model = Chat
		fields = ('messages', )


class TagForm(forms.ModelForm):

	class Meta:
		model = Tag
		fields = ('name', 'domain', 'description')