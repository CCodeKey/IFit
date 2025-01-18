from django.db import models
from django.contrib.auth.models import User 

class Recomendacao(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500)
    link = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = 'Recomendações'