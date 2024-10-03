from django import forms
from froala_editor.widgets import FroalaEditor

from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('post_type', 'title', 'subtitle', 'text', 'image')
        widgets = {
             'text': FroalaEditor,
          }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'title', 'text',)