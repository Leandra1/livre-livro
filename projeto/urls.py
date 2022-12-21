from django.contrib import admin
from django.urls import path
from livro.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name="url_index"),
    path('login/',login, name="url_login"),
    path('cadastre-se/',cadastro, name="url_cadastro"),
    path('livre-livro/',layout, name= "url_layout"),
    path('doar/',doar,name= "url_doar"),
    path('livros/',livros,name= "url_livros"),
    path('listagem/',listagem,name= "url_listagem"),




]
