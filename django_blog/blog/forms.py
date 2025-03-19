from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post

class MyForm(UserCreationForm):
    username = forms.CharField(min_length=5, max_length=100)
    first_name = forms.CharField(required=True, max_length=200)
    last_name = forms.CharField(required=True, max_length=200)
    email = forms.EmailField(required= True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
    def save(self, commit=True):
        post = super().save(commit=False)
        # Automatically set the author to the logged-in user
        post.author = self.request.user
        if commit:
            post.save()
        return post

class CommentForm(forms.ModelForm):
    class Meta:
        fields = '__all__'



