# IFit
## Como utilizar:
1. Instalar o Poetry
  ```bash
  pip install poetry
  ```
2. Instale as dependências com Poetry
  ```bash
  poetry install
  ```
3. Crie um ambiente virtual
  ```bash
  python -m venv venv
  ```
4. Ative o ambiente virtual
  - No Linux
  ```bash
  source venv/bin/activate
  ```
  - No Windows
  ```bash
  venv\Scripts\activate
  ```
5. Instale as dependências
```bash
pip install -r requirements.txt
```
---
## Configurações do Banco de Dados:
### No projeto o BD que está sendo usado é PostgreSQL, para você poder usa-lo é necessário:
1. Crie um arquivo *.env* e dentro insira as seguintes informações: 
```bash
  SECRET_KEY = ''                    # Onde você vai inserar uma chave secreta para o projeto
  DATABASE_URL = ''                  # Onde você vai inserir a URL de linkagem do Banco, que a propria plataforma do Neon PostgreSQL libera
  MAILERSEND_EMAIL = ''              # Onde você vai inserir seu email que a plataforma do MAILERSEN te forneceu
  MAILERSEND_EMAIL_PASSWORD = ''     # Onde você vai inserir a senha que o MAILERSEN te forneceu
```
2. Agora é só executar o projeto:
```bash
python manage.py runserver
```
### Caso não consiga realizar as configurações assima, e prefira uma forma mais simples para executar o projeto:
1. Altere as configurações de linkagem do BD:
  - Exclua essa parte no código:
> Se encontra no arquivo ../IFit/settings.py   |   linha : 65
  ```bash
    tmpPostgres = urlparse(os.getenv("DATABASE_URL"))

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': tmpPostgres.path.replace('/', ''),
            'USER': tmpPostgres.username,
            'PASSWORD': tmpPostgres.password,
            'HOST': tmpPostgres.hostname,
            'PORT': 5432,
        }
    }
  ```
  - E cole isso:
    ```bash
      DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.sqlite3',
          'NAME': BASE_DIR / 'db.sqlite3',
      }
    }
    ```
2. Execute esses comandos para fazer as migrações necessárias e conexões com o BD:
  - Makemigrations
    ```bash
    python manage.py makemigration
    ```
  - Migrate
   ```bash
      python manage.py migrate
   ```
3. Por fim, é só executar o projeto:
```bash
python manage.py runserver
```





