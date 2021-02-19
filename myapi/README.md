# Implement Token-based authentication using Django REST

## Setting Up The REST API Project
So let’s start from the very beginning. Install Django and DjangoRestFramework (DRF):
```
pip install django
pip install djangorestframework
```
Create a new Django project:
```
django-admin.py startproject myapi .
cd myapi
```
Start a new app, let´s call it core:
```
django-admin.py startapp core
```
Add the 'core' app and the 'rest_framework' app to the INSTALLED_APPS, inside the settings.py module:
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
    'rest_framework', # Third-Party Apps    
    'myapi.core', # Local Apps (Your project's apps)
]
```
## Migrate the database:
```
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
## Register a path in the urls.py module:
```python
# myapi/urls.py
from django.urls import path
from myapi.core import views

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
]
```
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
## Implementing the Token Authentication
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
## Migrate the database to create the table that will store the authentication tokens:
```
python manage.py migrate
```
## Create user
```
python manage.py createsuperuser --username ellis --email ellis@gmail.com
```





## Start up the Django server:
```
python manage.py runserver
```
From https://simpleisbetterthancomplex.com/tutorial/2018/11/22/how-to-implement-token-authentication-using-django-rest-framework.html

NEXT
https://www.geeksforgeeks.org/implement-token-authentication-using-django-rest-framework/