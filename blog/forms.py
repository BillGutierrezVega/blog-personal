# En tu archivo forms.py dentro de la aplicación blog
from django import forms
from .models import Post, Tag, Comentario

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'})
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
        

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['comentario']
        widgets = {
            'comentario': forms.Textarea(attrs={'class': 'form-control'})
        }
