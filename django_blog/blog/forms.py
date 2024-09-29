from django import forms
from .models import Post
from taggit.forms import TagField
from taggit.forms import TagWidget

class PostForm(forms.ModelForm):
    tags = TagField(widget=TagWidget(attrs={'placeholder': 'Add tags'}))
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = "Post Title"
        self.fields['content'].label = "Post Content"

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']