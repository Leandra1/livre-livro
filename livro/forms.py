from django.forms import ModelForm
from django import forms
from django.contrib.auth import forms
from livro.models import *


class LivroForm(ModelForm):
    class Meta:
        model = Livros
        fields = ['titulo', 'sinopse','estado','genero',  'autor' ]
        labels = {
            "titulo": "Titulo:",
            "sinopse": "Sinopse:",
            "estado": "Estado de conservação:",
            "genero": "Gênero:",
            "autor": "Autor:",
          
        }

