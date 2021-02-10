from django.forms import forms

from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('name', 'description', 'price', 'image')