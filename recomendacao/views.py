from django.shortcuts import render, redirect
from .models import Usuario
from django.views.generic import CreateView

def index(request):
    return render(request, "recomendacao/index.html")

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email',None)
        senha = request.POST.get('password',None)

        # desenvolver o metodo para busca da existencia do usuario
        # e processo de validação de dados
        return redirect('home')

    return render(request, "recomendacao/login.html")

def signIn(request):
    # Validar esses dados no banco de dados antes salvar
    if request.method == 'POST':
        nome = request.POST.get('nome',None)
        sobrenome = request.POST.get('sobrenome',None)
        email = request.POST.get('email',None)
        senha = request.POST.get('password',None)

        user = Usuario(
            nome = nome,
            sobrenome = sobrenome,
            email = email,
            senha = senha
        )
        user.save()

        return redirect('login')
        

    return render(request, "recomendacao/usuario_form.html")

def home(request):
    return render(request, "recomendacao/home.html")

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