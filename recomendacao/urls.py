from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('login', login, name="login"),
    path('signin', UsuarioCreateView.as_view(), name='newUser'),
    path('home', home, name='home'),
   
]