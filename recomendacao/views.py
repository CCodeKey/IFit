from django.shortcuts import render, redirect
from .models import Recomendacao, Perfil
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as _login
from django.contrib.auth import logout as _logout
from django.contrib.auth.decorators import login_required
from datetime import date
from .IA import modelo_de_linguagem

def index(request):
    # retornando os metadados da requisicao e a pagina html
    return render(request, "recomendacao/index.html")

def login(request):
    if request.method == 'POST': # validando se a requisicao foi POST
        # obtendo valores do html
        Email = request.POST.get('email',None)
        Senha = request.POST.get('password',None)
        # obtendo username pelo email
        nomeUser = User.objects.filter(email=Email).first()
        user = authenticate(request, username=nomeUser, password=Senha) # autenticando
        if user is not None:
            _login(request, user) # efetuando login
            return redirect('home')
        else:
           return render(request, "recomendacao/login.html")
    return render(request, "recomendacao/login.html")

def signIn(request):
    if request.method == 'POST': # validando se a requisicao foi POST
        # obtendo valores do html
        nome = request.POST.get('nome',None)
        sobrenome = request.POST.get('sobrenome',None)
        email = request.POST.get('email',None)
        _telefone = request.POST.get('telefone',None)
        _dtNascimento = request.POST.get('idade',None)
        _genero = request.POST.get('sexo',None)
        senha = request.POST.get('password',None)
    
        context = {'telefone':_telefone, 'email':email}
        # validando se o email existe
        BEmail = User.objects.filter(email=email).first()
        # se o email existir o user voltara para a tela de signIn
        if BEmail:
            context['telefone'] = ''
            context['email'] = ' E-mail inválido!'
            return render(request, "recomendacao/usuario_form.html", context)      
        # fazendo a mesma validacao para o telefone
        BTell = Perfil.objects.filter(telefone=_telefone).first()
        if BTell:
            context['telefone'] = 'N° de Telefone inválido!'
            context['email'] = ''
            return render(request, "recomendacao/usuario_form.html", context)
        # criando o usuario
        user = User.objects.create_user(username=f"{nome}_{sobrenome}_:{_telefone}", email= email, password=senha, first_name=nome, last_name=sobrenome)
        user.save()
        # criando perfil mediante ao usuario criado
        perfil = Perfil(telefone=_telefone, data_de_nascimento=_dtNascimento, genero=_genero, usuario=user)
        perfil.save()

        return redirect('login')
    return render(request, "recomendacao/usuario_form.html")

def logout(request):
    _logout(request) # metadados
    return redirect('index')

@login_required(login_url="auth/login") # metodo de validacao
def home(request):
    # obtendo user e suas recomendacoes
    user = Perfil.objects.filter(usuario=request.user).first()
    recomendacao = Recomendacao.objects.filter(perfil=user)
    # enviando essas recomendacoes como contexto
    context = {'recomendacoes':recomendacao}
    return render(request, "recomendacao/home.html", context)        

def formatar(data, _telefone):
    def idade(data_de_nasc):
        idade = 0
        # funcao para obter a data atual
        current_date = date.today()
        # ano/mes/dia recebido pela string
        ano_nascimento = data_de_nasc[:4]
        mes_nascimento = data_de_nasc[5:7]
        dia_nascimento = data_de_nasc[8:10]
        # ano/mes/dia de AGORA recebido pela DATETIME
        ano_actual = current_date.year
        mes_actual = current_date.month
        dia_actual = current_date.day
        # convertendo o string das datas pra int
        ano_nascimento = int(ano_nascimento)
        mes_nascimento = int(mes_nascimento)
        dia_nascimento = int(dia_nascimento)
        # logica para definir a idade mediante a data de agora e a data de nascimento
        if mes_nascimento == mes_actual:
            if dia_nascimento == dia_actual or dia_actual > dia_nascimento:
                idade = ano_actual - ano_nascimento
            elif dia_actual < dia_nascimento:
                idade = (ano_actual - ano_nascimento)-1 
        elif mes_actual < mes_nascimento:
            idade = (ano_actual - ano_nascimento)-1
        elif mes_actual > mes_nascimento :
            idade = ano_actual - ano_nascimento
        # retornando a idade do user
        return idade
    
    def telefone(numero):
        # funcao pra "mascarar"
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

@login_required(login_url="auth/login")
def recomendacao(request):
    if request.method == 'POST':
        # pegando valores do html
        altura = request.POST.get('altura',None)
        peso = request.POST.get('peso',None)
        nivel_atividade = request.POST.get('nivel_atividade',None)
        objetivo = request.POST.get('objetivo',None)
        restricao = request.POST.get('restricao',None)
        local_treino = request.POST.get('local_treino',None)
        duracao_treino = request.POST.get('duracao_treino',None)
        # obtendo perfil do user
        perfil = Perfil.objects.filter(usuario=request.user).first()
        # obtendo data de nascimento pelo perfil
        _data_de_nascimento = str(perfil.data_de_nascimento)
        # obtendo o genero do user
        _genero = str(perfil.genero)
        # enviando dados obtidos para o Modelo de Linguagem
        recomendacao_da_ia = modelo_de_linguagem(altura, peso, nivel_atividade, objetivo, restricao, local_treino, duracao_treino, _genero.lower(), formatar(_data_de_nascimento,0))
        # salvando resultado obtido da IA no BD
        rec = Recomendacao(titulo=recomendacao_da_ia[0], descricao=recomendacao_da_ia[1],link=recomendacao_da_ia[2], perfil=perfil)
        rec.save()
        return redirect('home')
    return render(request, "recomendacao/formulario.html")

@login_required(login_url='auth/login')
def apagarRecomendacao(request, recomendacao_id): 
    # obtendo a recomendacao existe pelo ID
    rec = Recomendacao.objects.filter(id=recomendacao_id).first()
    rec.delete()
    return redirect('home')

@login_required(login_url='auth/login')
def perfilUsuario(request):
    # obtendo user logado
    user = User.objects.filter(username=request.user).first()
    # obtendo perfil do user
    perfil = Perfil.objects.filter(usuario=user).first()
    # pegando data de nascimento e telefone do user 
    data_de_nascimento = str(perfil.data_de_nascimento)
    numero_de_telefone = str(perfil.telefone)
    # passando como contexto os dados dps de formatados pela funcao
    context = {'usuario':user, 'perfil':perfil, 'idade':formatar(data_de_nascimento,0), 'telefone':formatar('', numero_de_telefone)}
    return render(request, "recomendacao/perfil_user.html", context)

@login_required(login_url='auth/login')
def apagarConta(request):
    # obtendo user
    usuario = User.objects.get(username = request.user)
    usuario.delete()
    return redirect('index')

@login_required(login_url='auth/login')
def editarPerfil(request):
    if request.method == 'POST':
        # obtendo valores do html
        Nome = request.POST.get('nome',None)
        SobreNome = request.POST.get('sobrenome',None)
        Genero = request.POST.get('sexo',None)
        Data_de_nascimento = request.POST.get('idade',None)
        # obtendo o user e seu perfil
        _usua = User.objects.get(username = request.user)
        _perf = Perfil.objects.get(usuario = _usua)
        # setando valores
        _usua.first_name = Nome
        _usua.last_name = SobreNome
        _perf.genero = Genero
        _perf.data_de_nascimento = Data_de_nascimento
        # salvando dados
        _usua.save()
        _perf.save()

        return redirect('perfil')
    return render(request, "recomendacao/update_perfil_user.html")
    
@login_required(login_url="auth/login")
def visualizarRecomendacao(request, recomendacao_id):
    # obtendo recomendacao pelo ID
    _recomendacao = Recomendacao.objects.filter(id=recomendacao_id).first()
    # retorando recomendacao no contexto
    context = {'recomendacao':_recomendacao}
    return render(request, "recomendacao/recomendacao.html", context)  