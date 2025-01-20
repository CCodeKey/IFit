from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('auth/login', login, name="login"),
    path('auth/logout', logout, name='logout'),
    path('auth/signin', signIn, name='signin'),
    path('home', home, name='home'),
    path('new/recommendation', recomendacao, name='new_recomendation'),  
    path('pergunta', pergunta, name='pergunta'),
    path('delete/<recomendacao_id>', apagarRecomendacao, name='delete_recomendation'),
    path('accounts/recover', verificarEmailEEnviarToken, name='sendToken'),
    path('accounts/token/verify', verificarToken, name='verifyToken'),
    path('accounts/update/password', atualizarSenha, name='updatePass')
]