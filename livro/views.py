from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "templates/template1/index.html")
def login(request):
    return render(request, "templates/template2/mono-main/theme/login.html")
def cadastro(request):
    return render(request, "templates/template2/mono-main/theme/cadastro.html")
