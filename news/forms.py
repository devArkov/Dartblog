from django import forms
from .models import Post


class NewsForm(forms.ModelForm):
    # model = Post

    class Meta:
        model = Post
        fields = ['title', 'slug', 'content', 'category', 'photo', 'author']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 7}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
        }
