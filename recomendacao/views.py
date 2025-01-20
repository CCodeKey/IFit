from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Recomendacao, Perfil
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
        _telefone = request.POST.get('telefone',None)
        _cpf = request.POST.get('cpf',None)
        _dtNascimento = request.POST.get('idade',None)
        _genero = request.POST.get('sexo',None)
        senha = request.POST.get('password',None)
    
        context = {'cpf':_cpf, 'telefone':_telefone, 'email':email}
        Bcpf = Perfil.objects.filter(cpf=_cpf).first()

        if Bcpf:
            context['cpf'] = ' CPF inválido!'
            context['telefone'] = ''
            context['email'] = ''
            return render(request, "recomendacao/usuario_form.html", context)
        
        BEmail = User.objects.filter(email=email).first()
        
        if BEmail:
            context['cpf'] = ''
            context['telefone'] = ''
            context['email'] = ' E-mail inválido!'
            return render(request, "recomendacao/usuario_form.html", context)
        
        BTell = Perfil.objects.filter(telefone=_telefone).first()
        
        if BTell:
            context['cpf'] = ''
            context['telefone'] = 'N° de Telefone inválido!'
            context['email'] = ''
            return render(request, "recomendacao/usuario_form.html", context)
        
        user = User.objects.create_user(username=nome, email= email, password=senha, last_name=sobrenome)
        user.save()

        perfil = Perfil(telefone=_telefone, cpf=_cpf, data_de_nascimento=_dtNascimento, genero=_genero, usuario=user)
        perfil.save()

        return redirect('login')
        

    return render(request, "recomendacao/usuario_form.html")

def logout(request):
    _logout(request)
    return redirect('index')
 
@login_required(login_url="auth/login")
def home(request):
    recomendacao = Recomendacao.objects.all()
    context = {'recomendacoes':recomendacao}
    return render(request, "recomendacao/home.html", context)        

@login_required(login_url="auth/login")
def recomendacao(request):
    if request.method=='POST':
    #     idade = request.POST.get('idade',None)
    #     altura = request.POST.get('altura',None)
    #     peso = request.POST.get('peso',None)
    #     sexo = request.POST.get('sexo',None)
    #     nivel_atividade = request.POST.get('nivel_atividade',None)
    #     objetivo = request.POST.get('objetivo',None)
    #     restricao = request.POST.get('restricao',None)
    #     local_treino = request.POST.get('local_treino',None)
    #     duracao_treino = request.POST.get('duracao_treino',None)
    #     email = request.POST.get('email',None)

    #     context = {'objetivo':objetivo, 'peso':peso, 'altura':altura}

        titulo_ = request.POST.get('titulo',None)
        descricao_ = request.POST.get('descricao',None)
        link_ = request.POST.get('link',None)

        # rec = Recomendacao(titulo=titulo_, descricao=descricao_,link=link_, usuario=request.user)
        # rec.save()
        # Aqui será chamada a IA para processar os dados
        return redirect('home')
    return render(request, "recomendacao/formulario.html")

@login_required(login_url='auth/login')
def pergunta(request): 
    if request.method == 'POST':
        titulo_ = request.POST.get('titulo',None)
        descricao_ = request.POST.get('descricao',None)
        link_ = request.POST.get('link',None)
        user = request.user.username
        print(titulo_)
        print(descricao_)
        print(link_)
        print(user)
        rec = Recomendacao(titulo=titulo_, descricao=descricao_,link=link_, usuario=request.user)
        rec.save()

        print()
        return redirect('home')

    return render(request, "recomendacao/pergunta.html")
    
@login_required(login_url='auth/login')
def apagarRecomendacao(request, recomendacao_id):
    _id = request.POST.get('id',None)
    rec = Recomendacao.objects.filter(id=recomendacao_id).first()
    rec.delete()
    return redirect('home')

def verificarEmailEEnviarToken(request):
    if request.method == 'POST':
        email = request.POST.get('remail',None)
        user = User.objects.filter(email=email).first()
        if user:
            return render(request, "recomendacao/email-recuperar-senha.html")
        # Enviar Token para o numero do usuario
        return redirect('verifyToken')
    return render(request, "recomendacao/email-recuperar-senha.html")

def verificarToken(request):
    if request.method == 'POST':
        token = request.POST.get('tokenNumber',None)
        # Validar se o numero recebido e o numero enviado sao os mesmos
        return redirect('updatePass')
    return render(request, "recomendacao/token-recuperar-senha.html")

def atualizarSenha(request):
    if request.method == 'POST':
        novaSenha = request.POST.get('reset-senha',None)
        # Atualizar senha
        return redirect('login')
    return render(request, "recomendacao/nova-senha.html")