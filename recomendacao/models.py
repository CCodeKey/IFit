from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=8)
    sobrenome = models.CharField(max_length=20)
    idade = models.IntegerField()
    email = models.EmailField()
    senha = models.CharField(max_length=50)
    
    def __str__(self):
        nome = self.nome 
        sobrenome = self.sobrenome
        return f"{nome} {sobrenome}"

# Falta fazer a recomendação - completo
# Construir o sistema de login e signin