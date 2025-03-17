from django.apps import AppConfig

# -- Configura o nosso APP para ser usado no projeto Django
class RecomendacaoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'recomendacao'