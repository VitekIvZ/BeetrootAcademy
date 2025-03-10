from django import forms
from .models import Note
from .models import Post
from tinymce.widgets import TinyMCE


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'required': True}),
        }
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            #'content': TinyMCE(attrs={'cols': 80, 'rows': 30}),
            'content': forms.Textarea(attrs={'class': 'tinymce'}),
        }