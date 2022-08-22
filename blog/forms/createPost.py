from django import forms
from blog.models import ArticleModel


class AricleWriteModelForm(forms.ModelForm):
    class Meta:
        model = ArticleModel
        exclude = ('author', 'slug')
