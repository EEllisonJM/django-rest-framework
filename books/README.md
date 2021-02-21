# Building a Many-to-Many Modeled REST API with Django Rest Framework
## Setting up a new environment
```
python3 -m venv env
source env/bin/activate # Activate the virtual environment
```
## Create a requirements.txt file, paste the following into the file
```
django
djangorestframework
psycopg2-binary
```
## Install the dependencies
```
pip install -r requirements.txt
```
## Create a project called 'sampleproject'
```
django-admin.py startproject sampleproject
cd sampleproject
django-admin.py startapp authors
```
## Add the app created to the setting.py module
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'authors.apps.AuthorsConfig', # /authors/apps.py/ ... class AuthorsConfig
    'rest_framework.authtoken',   #authentication
    'rest_framework',#rest_framework
]

```
## Create the models
# Create your models here.
```py
# /authors/models.py
class Book(models.Model):

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    publisher = models.CharField(max_length=400)
    release_date = models.DateField()


class Author(models.Model):
    name = models.CharField(max_length=225)
    biography  = models.TextField()
    date_of_birth = models.DateField()
    books = models.ManyToManyField('Book', related_name='authors', blank=True)

```
## Migrate the models created
```
python manage.py makemigrations
python manage.py migrate
```
## Create authors/serializer.py
```py
# /authors/serializer.py
from rest_framework import serializers

from django.contrib.auth.models import User
from .models import Author, Book


# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        ordering = ['-id']
        model = Author
        fields = ("id", "name", "biography", "date_of_birth", "books")
        extra_kwargs = {'books': {'required': False}}
        depth = 1 # Specifying nested serialization 

class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)

    class Meta:
        ordering = ['-id']
        model = Book
        fields = ("id", "title", "description", "publisher", "release_date", "authors")
        extra_kwargs = {'authors': {'required': False}}
```
## Create the views
```py
# /authors/views.py
from rest_framework import routers, serializers, viewsets, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializer import UserSerializer, AuthorSerializer, BookSerializer
from .models import Author, Book
from rest_framework import filters

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class AuthorViewSet(viewsets.ModelViewSet):
    """
    List all workers, or create a new worker.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    List all workkers, or create a new worker.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['release_date']
```
## Wire up the routes
```py
# /sampleproject/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from authors.views import UserViewSet, AuthorViewSet, BookViewSet
from rest_framework.routers import DefaultRouter

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token


# Routers provide an easy way of automatically determining the URL conf.

router = DefaultRouter()
router.register(r'api/users', UserViewSet, basename='user')
router.register(r'api/authors', AuthorViewSet, basename='author')
router.register(r'api/books', BookViewSet, basename='book')


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),    
    path(r'', include(router.urls)),
    path(r'api/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth')

]
```
From : https://medium.com/@kingsleytorlowei/building-a-many-to-many-modelled-rest-api-with-django-rest-framework-d41f54fe372