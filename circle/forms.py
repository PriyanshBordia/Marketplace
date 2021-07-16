from django import forms

from .models import Article, Person, Tag, Message, Chat

class ArticleForm(forms.ModelForm):
	def __str__(self) -> str:
		return super().__str__()

	class Meta:
		model = Article
		fields = ('title', 'description', 'image', 'price', 'tags')


class PersonForm(forms.ModelForm):

	def __str__(self) -> str:
		return super().__str__()

	class Meta:
		model = Person
		fields = ('username', 'bio', 'age', 'sex', 'email', 'ph_no')


class TagForm(forms.ModelForm):

	def __str__(self) -> str:
		return super().__str__()

	class Meta:
		model = Tag
		# fields = ('name', 'domain', 'description')
		fields = '__all__'

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
