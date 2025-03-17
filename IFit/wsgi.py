import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IFit.settings')
application = get_wsgi_application()

# -- Configuração que faz o Django rodar em servidores Web:Gunicorn