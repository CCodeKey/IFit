from django.shortcuts import render, redirect
from .models import Usuario
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as _login
from django.contrib.auth import logout as _logout
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "recomendacao/index.html")

def login(request):
    if request.method == 'POST':
        Email = request.POST.get('email',None)
        Senha = request.POST.get('password',None)

        nomeUser = User.objects.filter(email=Email).first()
        user = authenticate(request, username=nomeUser, password=Senha)
        
        if user is not None:
            _login(request, user)
            return redirect('home')
        else:
           return render(request, "recomendacao/login.html")
    return render(request, "recomendacao/login.html")

def signIn(request):
    # Validar esses dados no banco de dados antes salvar
    if request.method == 'POST':
        nome = request.POST.get('nome',None)
        sobrenome = request.POST.get('sobrenome',None)
        email = request.POST.get('email',None)
        senha = request.POST.get('password',None)

        user = User.objects.filter(email=email).first()

        context = {'nome':nome, 'sobrenome':sobrenome, 'password':senha}

        if user:
            return render(request, "recomendacao/usuario_form.html", context)
        
        user = User.objects.create_user(username=nome,email= email, password=senha,last_name=sobrenome)
        user.save()

        return redirect('login')
        

    return render(request, "recomendacao/usuario_form.html")

def logout(request):
    _logout(request)
    return redirect('index')
 
@login_required(login_url="auth/login")
def home(request):
    return render(request, "recomendacao/home.html")        

@login_required(login_url="auth/login")
def recomendacao(request):
    if request.method=='POST':
        idade = request.POST.get('idade',None)
        altura = request.POST.get('altura',None)
        peso = request.POST.get('peso',None)
        sexo = request.POST.get('sexo',None)
        nivel_atividade = request.POST.get('nivel_atividade',None)
        objetivo = request.POST.get('objetivo',None)
        restricao = request.POST.get('restricao',None)
        local_treino = request.POST.get('local_treino',None)
        duracao_treino = request.POST.get('duracao_treino',None)
        email = request.POST.get('email',None)

        # Aqui será chamada a IA para processar os dados
        return redirect('home')        

    return render(request, "recomendacao/formulario.html")