from django import forms

from blogapp.models import Article

class ArticleForms(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']