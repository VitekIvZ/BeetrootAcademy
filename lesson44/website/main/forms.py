from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, MyGroup


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'password1', 'password2', 'groups']
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'group']
        
class GroupForm(forms.ModelForm):
    class Meta:
        model = MyGroup
        fields = ['name']
    
