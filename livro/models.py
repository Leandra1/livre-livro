from uuid import uuid4
from django.db import models

# livros
class livros(models.Model):
    id_livro = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    titulo = models.CharField(max_length=100,blank=True, null=True)
    autor = models.CharField(max_length=100,blank=True, null=True)
    sinopse = models.CharField(max_length=500,blank=True, null=True)
    estado = models.CharField(max_length=100,blank=True, null=True)
    genero = models.CharField(max_length=100,blank=True, null=True)

