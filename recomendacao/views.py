from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Recomendacao, Perfil
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as _login
from django.contrib.auth import logout as _logout
from django.contrib.auth.decorators import login_required
from datetime import date

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
        _dtNascimento = request.POST.get('idade',None)
        _genero = request.POST.get('sexo',None)
        senha = request.POST.get('password',None)
    
        context = {'telefone':_telefone, 'email':email}

        BEmail = User.objects.filter(email=email).first()
        
        if BEmail:
            context['telefone'] = ''
            context['email'] = ' E-mail inválido!'
            return render(request, "recomendacao/usuario_form.html", context)
        
        BTell = Perfil.objects.filter(telefone=_telefone).first()
        
        if BTell:
            context['telefone'] = 'N° de Telefone inválido!'
            context['email'] = ''
            return render(request, "recomendacao/usuario_form.html", context)
        
        user = User.objects.create_user(username=nome, email= email, password=senha, last_name=sobrenome)
        user.save()

        perfil = Perfil(telefone=_telefone, data_de_nascimento=_dtNascimento, genero=_genero, usuario=user)
        perfil.save()

        return redirect('login')
        

    return render(request, "recomendacao/usuario_form.html")

def logout(request):
    _logout(request)
    return redirect('index')
 
@login_required(login_url="auth/login")
def home(request):
    user = Perfil.objects.filter(usuario=request.user).first()
    recomendacao = Recomendacao.objects.filter(perfil=user)
    context = {'recomendacoes':recomendacao}
    return render(request, "recomendacao/home.html", context)        

@login_required(login_url="auth/login")
def recomendacao(request):
    if request.method == 'POST':
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

       

        # user = Perfil.objects.filter(usuario=request.user).first()
        # rec = Recomendacao(titulo=titulo_, descricao=descricao_,link=link_, perfil=user)
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

        user = Perfil.objects.filter(usuario=request.user).first()
        rec = Recomendacao(titulo=titulo_, descricao=descricao_,link=link_, perfil=user)
        rec.save()

        return redirect('home')

    return render(request, "recomendacao/pergunta.html")
 
@login_required(login_url='auth/login')
def apagarRecomendacao(request, recomendacao_id):
    rec = Recomendacao.objects.filter(id=recomendacao_id).first()
    rec.delete()
    return redirect('home')

def formatar(data, _telefone):
    def idade(data_de_nasc):
        idade = 0
        current_date = date.today()
        ano_nascimento = data_de_nasc[:4]
        mes_nascimento = data_de_nasc[5:7]
        dia_nascimento = data_de_nasc[8:10]

        ano_actual = current_date.year
        mes_actual = current_date.month
        dia_actual = current_date.day

        ano_nascimento = int(ano_nascimento)
        mes_nascimento = int(mes_nascimento)
        dia_nascimento = int(dia_nascimento)

        if mes_nascimento == mes_actual:
            if dia_nascimento == dia_actual or dia_actual > dia_nascimento:
                idade = ano_actual - ano_nascimento
            elif dia_actual < dia_nascimento:
                idade = (ano_actual - ano_nascimento)-1 
        elif mes_actual < mes_nascimento:
            idade = (ano_actual - ano_nascimento)-1
        elif mes_actual > mes_nascimento :
            idade = ano_actual - ano_nascimento
        return idade
    
    def telefone(numero):
        operadora = numero[:2]
        priN = numero[6:7]
        segN = numero[10:11]
        _numero = f"({operadora}) ****{priN}-***{segN}"
        return _numero
    
    if _telefone == 0:
        idade = idade(data)
        return idade
    else:
        numero = telefone(_telefone)
        return numero

@login_required(login_url='auth/login')
def perfilUsuario(request):
    user = User.objects.filter(username=request.user).first()
    perfil = Perfil.objects.filter(usuario=user).first()
    
    data_de_nascimento = str(perfil.data_de_nascimento)
    numero_de_telefone = str(perfil.telefone)

    context = {'usuario':user, 'perfil':perfil, 'idade':formatar(data_de_nascimento,0), 'telefone':formatar('', numero_de_telefone)}
    return render(request, "recomendacao/perfil_user.html", context)

@login_required(login_url='auth/login')
def apagarConta(request):
    usuario = User.objects.get(username = request.user)
    usuario.delete()
    return redirect('index')

@login_required(login_url='auth/login')
def editarPerfil(request):
    if request.method == 'POST':
        Nome = request.POST.get('nome',None)
        SobreNome = request.POST.get('sobrenome',None)
        Genero = request.POST.get('sexo',None)
        Data_de_nascimento = request.POST.get('idade',None)
        
        _usua = User.objects.get(username = request.user)
        _perf = Perfil.objects.get(usuario = _usua)

        _usua.username = Nome
        _usua.last_name = SobreNome
        _perf.genero = Genero
        _perf.data_de_nascimento = Data_de_nascimento

        _usua.save()
        _perf.save()

        return redirect('perfil')

    return render(request, "recomendacao/update_perfil_user.html")
    
@login_required(login_url="auth/login")
def visualizarRecomendacao(request, recomendacao_id):
    _recomendacao = Recomendacao.objects.filter(id=recomendacao_id).first()
    context = {'recomendacao':_recomendacao}
    return render(request, "recomendacao/recomendacao.html", context)  