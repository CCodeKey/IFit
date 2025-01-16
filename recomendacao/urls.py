from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('auth/login', login, name="login"),
    path('auth/signin', signIn, name='signin'),
    path('p/home', home, name='home'),
    path('p/nova-recomendacao', recomendacao, name='newRecomendation'),
]