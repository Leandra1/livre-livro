from django.contrib.auth.models import User
from uuid import uuid4
from django.db import models

# livros
class Livros (models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100,blank=True, null=True)
    autor = models.CharField(max_length=100,blank=True, null=True)
    sinopse = models.CharField(max_length=500,blank=True, null=True)
    estado = models.CharField(max_length=100,blank=True, null=True)
    genero = models.CharField(max_length=100,blank=True, null=True)
    contato = models.CharField(max_length=100,blank=True, null=True)
    doador_id = models.ForeignKey(User, on_delete = models.CASCADE )

