from django.db import models
from django.contrib.auth.models import User 

class Perfil(models.Model):
    telefone = models.CharField(max_length=15)
    cpf = models.CharField(max_length=11) 
    genero = models.CharField(max_length=7)
    data_de_nascimento = models.CharField(max_length=11) 
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.usuario.username
    
    class Meta:
        verbose_name = 'Perfi'

class Recomendacao(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500)
    link = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True)    

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = 'Recomendaçõe'

