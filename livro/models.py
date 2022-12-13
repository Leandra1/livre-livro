from uuid import uuid4
from django.db import models

# Create your models here.
class livros(models.Model):
    id_livro = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    descricao = models.CharField(max_length=500)
    data = models.DateField(auto_now_add=True)
