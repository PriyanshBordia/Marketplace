from django import forms
from django.contrib.auth.models import User

from .models import Article, Person, Tag, Message, Chat

class UserForm(forms.ModelForm):

	class Meta:
		model = User
		fields = '__all__'

	def __str__(self) -> str:
		return super().__str__()


class ArticleForm(forms.ModelForm):

	class Meta:
		model = Article
		fields = ('title', 'description', 'image', 'price')
	
	def __str__(self) -> str:
		return super().__str__()


class PersonForm(forms.ModelForm):

	def __str__(self) -> str:
		return super().__str__()

	class Meta:
		model = Person
		fields = ('first', 'last', 'bio', 'profile', 'age', 'sex', 'email', 'ph_no', 'allowsMessage')


class MessageForm(forms.ModelForm):

	def __str__(self) -> str:
		return super().__str__()

	class Meta:
		model = Message
		fields = ('text', )


class ChatForm(forms.ModelForm):

	def __str__(self) -> str:
		return super().__str__()

	class Meta:
		model = Chat
		fields = ('messages', )


class TagForm(forms.ModelForm):

	def __str__(self) -> str:
		return super().__str__()

	class Meta:
		model = Tag
		fields = ('name', 'domain', 'description')