# user-management
 A Django Rest Framework user management platform with OAuth2 

Pra rodar a aplicacao:

```	python
    python3 -m venv venv
    venv/Scripts/activate
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
```

Se for o primeiro run de uma database, criar superuser:

``` 
python manage.py createsuperuser

```

Instalei novos requirements?

```
pip freeze requirements.txt > requirements.txt
```