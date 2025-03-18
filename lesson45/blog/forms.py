from django.forms import Form, CharField, SlugField, Textarea, TextInput, SelectMultiple
from django.forms import ModelForm, PasswordInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Post, Tag


class PostForm(ModelForm):
# class PostForm(Form):
#     title = CharField(max_length=100)
#     slug = SlugField(max_length=100)
#     body = CharField(required=False, 
#                      widget=Textarea(attrs={'rows': 5, 'cols': 40}), 
#                      label="Text")

#     def save(self):
#         post = Post.objects.create(
#             title=self.cleaned_data['title'], 
#             slug=self.cleaned_data['slug'], 
#             body=self.cleaned_data['body']
#         )
#         return post

    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'tags']
        widgets = {'title': TextInput(), 'slug': TextInput(), 
                   'body': Textarea(), 'tags': SelectMultiple()}
    
    def clean_slug(self):
        slug = self.cleaned_data['slug'].lower()
        if slug == 'create':
            raise ValidationError("Slug 'create' does not allowed")
        return slug


class TagForm(ModelForm):

    class Meta:
        model = Tag
        fields = ['title', 'slug']
        widgets = {'title': TextInput(), 'slug': TextInput()}


class LoginUserForm(Form):
    username = CharField(max_length=100, widget=TextInput())
    password = CharField(max_length=100, widget=PasswordInput())


# class RegisterUserForm(ModelForm):
#     username = CharField(label="Псевдонім користувача", max_length=100, widget=TextInput())
#     password = CharField(label="Пароль", max_length=100, widget=PasswordInput())
#     password2 = CharField(label="Повторний Пароль", max_length=100, widget=PasswordInput())

#     class Meta:
#         model = User
#         fields = ['username', 'password', 'password2', 
#                   'first_name', 'last_name', 'email']
    
#     def clean_password(self):
#         cd = self.cleaned_data
#         if len(cd['password']) < 8:
#             raise ValidationError(f"Password should be longer then 8 symbols")
#         return cd['password']
    
#     def clean_password2(self):
#         cd = self.cleaned_data
#         if cd.get('password') != cd['password2']:
#             raise ValidationError(f"Password and password2 fields should be equal!")
#         return cd['password2']
    
#     def clean_email(self):
#         cd = self.cleaned_data
#         email = cd['email']
#         if email and User.objects.all().filter(email=email):
#             raise ValidationError(f"Email already exsists")
#         return email
        

class RegisterUserForm(UserCreationForm):
    username = CharField(label="Псевдонім користувача", max_length=100, widget=TextInput())
    password1 = CharField(label="Пароль", max_length=100, widget=PasswordInput())
    password2 = CharField(label="Повторний Пароль", max_length=100, widget=PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 
                  'first_name', 'last_name', 'email']
        labels = {
            'email': "E-mail",
        }
        
    