# Set up Django

## Install Django:
```
$ pip install django
```
## Start a new Django project:
```
$ django-admin startproject mysite
```
## Test run the Django server:
```
$ python manage.py runserver
```
Go to http://localhost:8000/

## Create API app
```
$ python manage.py startapp myapi
```
## Register the myapi app with the mysite project
```python
# mysite/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapi.apps.MyapiConfig', # NEW
]
```
## Migrate the database
```
$ python manage.py migrate
```
## Create Super User
```
$ python manage.py createsuperuser
```
## Start up the Django server:

```
python manage.py runserver
```
And then navigate to http://localhost:8000/admin/

# Create a model in the database that Django ORM will manage
## Create Hero model
```python
# myapi/models.py
from django.db import models

class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    def __str__(self):
        return self.name
```
## Make migrations
```
$ python manage.py makemigrations
```
```
$ python manage.py migrate
```
## Register Hero with the admin site
```python
# myapi/admin.py 
from django.contrib import admin
from .models import Hero

admin.site.register(Hero)
```
## Run the Django server:
```
$ python manage.py runserver
```
And then navigate to http://localhost:8000/admin/
## Create some new heroes

# Set up Django REST Framework
```
$ pip install djangorestframework
```
## Add Django  REST Framework
```python
 # mysite/settings.py:
 INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapi.apps.MyapiConfig',
    'rest_framework', # NEW
]
```
## Add pagination
```python
# mysit/settings.py
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
```
# Serialize the Hero model
Serialization is the process of converting a Model to JSON. Using a serializer, we can specify what fields should be present in the JSON representation of the model.
##  Create serialazer file
```python
# myapi/serializers.py
from rest_framework import serializers

from .models import Hero

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        #fields = ('name', 'alias') # Serialize fields explicitly
        fields = '__all__' # Serialize all fields implicitly
```
# Display the data
## Views
```python
#myapi/views.py:
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HeroSerializer
from .models import Hero
# ModelViewSet is a special view that Django Rest Framework provides.
# It will handle GET and POST for Heroes without us having to do any more work.
class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer
```
## Site URLs: Point a URL at the viewset we just created.
```python
# mysite/urls.py
from django.contrib import admin
from django.urls import path,include # NEW

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapi.urls')), # NEW
]
```
## API URLs:
Django is going to look next for instructions on how to route the above URL (myapi.urls).
```python
# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'heroes', views.HeroViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
```
From https://medium.com/swlh/build-your-first-rest-api-with-django-rest-framework-e394e39a482c