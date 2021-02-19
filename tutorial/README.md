# Tutorial 1: Serialization

## Setting up a new environment
```python
python3 -m venv env
source env/bin/activate # Activate the virtual environment
```
Now that we're inside a virtual environment, we can install our package requirements.
```python
(env) xxx $ pip install django
(env) xxx $ pip install djangorestframework
(env) xxx $ pip install pygments  # We'll be using this for the code highlighting
```
## Setting up a new environment
Before we do anything else we'll create a new virtual environment, using venv. This will make sure our package configuration is kept nicely isolated from any other projects we're working on.
```python
python3 -m venv env
source env/bin/activate
```
Now that we're inside a virtual environment, we can install our package requirements.
```python
pip install django
pip install djangorestframework
pip install pygments  # We'll be using this for the code highlighting
```
## To get started, let's create a new project to work with.
cd ~
django-admin startproject tutorial
cd tutorial

## Once that's done we can create an app that we'll use to create a simple Web API.
```python
python manage.py startapp snippets
```
## We'll need to add our new snippets app and the rest_framework app to INSTALLED_APPS. Let's edit the tutorial/settings.py file:
```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'snippets.apps.SnippetsConfig',
]
```
## Creating a model to work with
```python
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ['created']
```
## Create an initial migration for our snippet model, and sync the database for the first time.
```
python manage.py makemigrations snippets
python manage.py migrate
```

## Creating a Serializer class
The first thing we need to get started on our Web API is to provide a way of serializing and deserializing the snippet instances into representations such as json. We can do this by declaring serializers that work very similar to Django's forms. 
```python
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
```
## Using ModelSerializers
It's important to remember that ModelSerializer classes don't do anything particularly magical, they are simply a shortcut for creating serializer classes:

An automatically determined set of fields.
Simple default implementations for the create() and update() methods.

# Tutorial 2: Requests and Responses
## Wrapping API views
REST framework provides two wrappers you can use to write API views.
- The @api_view decorator for working with function based views.
- The APIView class for working with class-based views.

# Tutorial 3
## Tutorial 3: Class-based Views
## Rewriting our API using class-based views
- Refactoring
## Using mixins
## Using generic class-based views

# Tutorial 4: Authentication & Permissions

# Tutorial 5: Relationships & Hyperlinked APIs
## Creating an endpoint for the root of our API
## Creating an endpoint for the highlighted snippets
# Hyperlinking our API

