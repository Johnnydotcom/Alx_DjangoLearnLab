from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tag']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = "Post Title"
        self.fields['content'].label = "Post Content"

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']