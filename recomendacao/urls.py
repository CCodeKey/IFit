from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('', index, name="index"),
    path('home', home, name='home'), 

    path('auth/login', login, name="login"),
    path('auth/logout', logout, name='logout'),
    path('auth/signin', signIn, name='signin'),

    path('recommend/', recomendacao, name='new_recomendation'),
    path('recommend/pergunta', pergunta, name='pergunta'),
    path('recommend/view/<recomendacao_id>', visualizarRecomendacao, name='visualization'),
    path('recommend/delete/<recomendacao_id>', apagarRecomendacao, name='delete_recommendation'),

    path('account/profile', perfilUsuario, name='perfil'),
    path('account/delete/user', apagarConta, name='delete_account'),
    path('account/update/profile', editarPerfil, name='editPerfil'),
    path('account/update/password', auth_views.PasswordChangeView.as_view(template_name='recomendacao/update_password.html'), name='password_change_password'),
    path('account/update/password/success', auth_views.PasswordChangeDoneView.as_view(template_name='recomendacao/update_password_success.html'), name='password_change_done'),
  
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='recomendacao/password_reset_form.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='recomendacao/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='recomendacao/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='recomendacao/password_reset_complete.html'), name='password_reset_complete')
]