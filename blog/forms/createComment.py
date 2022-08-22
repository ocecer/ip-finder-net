from dataclasses import field
from socket import fromshare
from django import forms
from blog.models import CommentModel, comment


class CommentCreateModelForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ('comment', )
