from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('', index, name="index"),
    path('auth/login', login, name="login"),
    path('auth/logout', logout, name='logout'),
    path('auth/signin', signIn, name='signin'),
    path('home', home, name='home'),
    path('account/profile', perfilUsuario, name='perfil'),
    path('delete/<recomendacao_id>', apagarRecomendacao, name='delete'),
    path('new/recommendation', recomendacao, name='new_recomendation'),  
    path('pergunta', pergunta, name='pergunta'),
    path('account/delete', apagarConta, name='delete_account'),
    path('account/update/password', alterarSenha, name='change_password'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='recomendacao/password_reset_form.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='recomendacao/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='recomendacao/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='recomendacao/password_reset_complete.html'), name='password_reset_complete'),
]