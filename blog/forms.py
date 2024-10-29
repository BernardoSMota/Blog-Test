from django import forms
from blog.models import Post
from tinymce.widgets import TinyMCE


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE())

    class Meta:
        model = Post
        fields = ['title', 'summary', 'cover', 'cover_in_post_content', 'content', 'published', 'tags', 'category',]