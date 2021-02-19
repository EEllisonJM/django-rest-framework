# Implement Token-based authentication using Django REST
## Setting up a new environment
```
python3 -m venv env
```
### Activate the virtual environment
```
source env/bin/activate
```
## Setting Up The REST API Project
### Install our package requirements. Django and DjangoRestFramework (DRF):
```
pip install django
pip install djangorestframework
```
### Create a new Django project:
```
mkdir myapi
cd myapi
django-admin.py startproject myapi .
cd myapi
```
### Start a new app 'core':
```
django-admin.py startapp core
```
### Add apps to the settings.py module:
```python
# myapi/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',    
    'rest_framework', # Third-Party Apps    
    'myapi.core', # Local Apps (Your project's apps)
]
```
## Migrate the database:
```
cd ..
python manage.py migrate
```
## Create our first API view
```python
# myapi/core/views.py
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloView(APIView):
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
```
## Wire view up in the urls.py module:
```python
# myapi/urls.py
from django.urls import path
from myapi.core import views

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
]
```
## Run the Django server:
```
python manage.py runserver
```
Go to http://localhost:8000/hello/
## Protect this API endpoint so we can implement the token authentication:
```python
#myapi/core/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  # <-- Here

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)             # <-- And here

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
```
## Implementing the Token Authentication app int the settings module
```python
# myapi/settings.py

INSTALLED_APPS = [
    # Django Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third-Party Apps
    'rest_framework',
    'rest_framework.authtoken',  # <-- Here
    # Local Apps (Your project's apps)
    'myapi.core',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',  # <-- And here
    ],
}
```
### Migrate the database to create the table that will store the authentication tokens:
```
python manage.py migrate
```
### Run the Django server:
```
python manage.py runserver
```
Go to http://localhost:8000/hello/
### Create user 'ellis' and password 'ellis' or whatever you prefer
```
python manage.py createsuperuser --username ellis --email ellis@gmail.com
```
### Generate a token for user 'ellis'
```
python manage.py drf_create_token ellis
```
Token generated
```
Generated token 8e6771e6222e9fa3b3495e80c373d65597970a62 for user ellis
```
## Run the Django server:
```
python manage.py runserver
```
### Make a request to our /hello/ endpoint:
```
http http://127.0.0.1:8000/hello/
```
Authentication credentials were not provided.
```
HTTP/1.1 401 Unauthorized
```
Using our token!
```
http http://127.0.0.1:8000/hello/ 'Authorization: Token 8e6771e6222e9fa3b3495e80c373d65597970a62'
```
"message": "Hello, World!"
```
HTTP/1.1 200 OK
```
## User Requesting a Token
It doesn’t handle GET requests. Basically it’s just a view to receive a POST request with username and password.
```python
# myapi/urls.py
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here
from myapi.core import views

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # <-- And here
]
```
Test it
```
http post http://127.0.0.1:8000/api-token-auth/ username=ellis password=ellis
```

From https://simpleisbetterthancomplex.com/tutorial/2018/11/22/how-to-implement-token-authentication-using-django-rest-framework.html