"""projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from livro.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name="url_index"),
    path('login/',login, name="url_login"),
    path('cadastre-se/',cadastro, name="url_cadastro"),
    path('inicio/',inicio, name="url_inicio"),
    path('livre-livro/',layout, name= "url_layout"),
    path('doar/',doar,name= "url_doar"),
    path('livros/',livros,name= "url_livros"),
    path('listagem/',listagem,name= "url_listagem"),




]
