from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('auth/login', login, name="login"),
    path('auth/logout', logout, name='logout'),
    path('auth/signin', signIn, name='signin'),
    path('home', home, name='home'),
    path('nova-recomendacao', recomendacao, name='newRecomendation')   
]