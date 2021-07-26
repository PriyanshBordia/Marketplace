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
		fields = ('profile', 'first', 'last', 'bio', 'age', 'sex', 'email', 'ph_no', 'allowsMessage')


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

"""
def clean(self):

    # data from the form is fetched using super function
    super(PostForm, self).clean()

     # extract the username and text field from the data
     username = self.cleaned_data.get('username')
      text = self.cleaned_data.get('text')

       # conditions to be met for the username length
       if len(username) < 5:
            self._errors['username'] = self.error_class([
                'Minimum 5 characters required'])
        if len(text) < 10:
            self._errors['text'] = self.error_class([
                'Post Should Contain a minimum of 10 characters'])

        # return any errors if found
        return self.cleaned_data
"""
