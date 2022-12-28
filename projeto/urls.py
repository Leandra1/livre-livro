from django.contrib import admin
from django.urls import path, include
from livro.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name="url_index"),
    path('account/', include('django.contrib.auth.urls')),
    path('cadastre-se/',cadastro, name="url_cadastro"),
    path('livre-livro/',layout, name= "url_layout"),
    path('doar/',doar,name= "url_doar"),
    path('livros/',livros,name= "url_livros"),
    path('listagem/',listagem,name= "url_listagem"),
    path('busca/',search,name= "url_search"),
    path('receber/',detalhes,name= "url_detalhes"),




]
