from django.shortcuts import render
from .models import Usuario
from django.views.generic import CreateView

def home(request):
    return render(request, "recomendacao/home.html")

def login(request):
    return render(request, "recomendacao/login.html")

class UsuarioCreateView(CreateView):
    model = Usuario
    fields = ['nome','sobrenome','idade','email','senha']
    success_url = "login"