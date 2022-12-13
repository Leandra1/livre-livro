from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "templates/template1/index.html")
def login(request):
    return render(request, "templates/template2/mono-main/theme/login.html")
def cadastro(request):
    return render(request, "templates/template2/mono-main/theme/cadastro.html")
def inicio(request):
    return render(request, "templates/template2/mono-main/theme/inicio.html")
def layout(request):
    return render(request, "templates/template2/mono-main/theme/layout.html")
def doar(request):
    return render(request, "templates/template2/mono-main/theme/doar.html")
def livros(request):
    return render(request, "templates/template2/mono-main/theme/livros.html")
def listagem(request):
    return render(request, "templates/template2/mono-main/theme/listagem.html")
