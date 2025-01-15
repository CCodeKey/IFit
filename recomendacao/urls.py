from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('login', login, name="login"),
    path('signin', signIn, name='newUser'),
    path('home', home, name='home'),
    path('nova-recomendacao', recomendacao, name='newRecomendation'),
]