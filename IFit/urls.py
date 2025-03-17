from django.contrib import admin
from django.urls import path, include

# -- URLs do projeto
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recomendacao.urls'))
]