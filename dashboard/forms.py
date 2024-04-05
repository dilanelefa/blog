from django import forms
from blog_app.models import Post


class CreatePostForm(forms.Form):
    title = forms.CharField(max_length=128, required=True)
    content = forms.CharField(required=True, widget=forms.Textarea)
    description = forms.CharField(max_length=64 ,required=True)
    thumbnail = forms.ImageField(required=False)