from django.contrib import admin
from .models import Recomendacao, Perfil

# -- Registrando os modelos no painel do ADM 
admin.site.register(Perfil)
admin.site.register(Recomendacao)