from django.http.response import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "templates/template1/index.html")

def cadastro(request):
    if request.method== "GET":
        return render(request, "templates/template2/mono-main/theme/cadastro.html")
    else:
       name = request.POST.get('name') 
       email = request.POST.get('email') 
       password = request.POST.get('password') 
       
      
    user = User.objects.create_user(username=name, email=email, password=password)

    return redirect("/login")

      
def login(request):
    if request.method =="GET":
        return render(request, "templates/template2/mono-main/theme/login.html")
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email=email, password=password)


def logout_views(request):
    if request.user.is_authenticated:
        logout(request)
     
    return render(request, "index.html")


@login_required(login_url="/login/")
def livros(request):
        return render(request, "templates/template2/mono-main/theme/livros.html")



def inicio(request):
    return render(request, "templates/template2/mono-main/theme/inicio.html")
def layout(request):
    return render(request, "templates/template2/mono-main/theme/layout.html")
def doar(request):
    return render(request, "templates/template2/mono-main/theme/doar.html")


    


def listagem(request):
    return render(request, "templates/template2/mono-main/theme/listagem.html")
