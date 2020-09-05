from django import forms
from django.forms import ModelForm
from . import models
from .models import Post


class PostForm(forms.Form):
    class Meta:
        model = Post
        fields = ('title', 'body',)
