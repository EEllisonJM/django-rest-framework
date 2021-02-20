# 1. Setting up a new environment
```
python3 -m venv env
source env/bin/activate
```
# 2. Install package requirements.
```
pip install django
pip install djangorestframework
```
# 3. Create a Django project:
```
mkdir api_codigo_postal
cd api_codigo_postal
django-admin.py startproject api_codigo_postal .
cd api_codigo_postal
```
# 4. Create an app
```
python manage.py startapp codigo_postal
```

# 5. Add app created to the settings.py module
```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework', # NEW
    'codigo_postal.apps', # NEW
]
```
# 6. Create a model in the database that Django ORM will manage to the models.py module
```py
#https://docs.djangoproject.com/en/3.1/topics/db/models/
# codigo_postal/models.py
from django.db import models

class CodigoPostal(models.Model):
    # An id field is added automatically.
    codigo = models.CharField(max_length=5)
    asentamiento = models.CharField(max_length=60)
    tipo_asentamiento = models.CharField(max_length=20)
    municipio = models.CharField(max_length=35)
    estado = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=25)
    zona = models.CharField(max_length=20) 
    def __str__(self):
        return self.codigo
```
# 7. Create an initial migration for our custom model, and sync the database for the first time (Migrate the database).
```
python manage.py makemigrations codigo_postal
python manage.py migrate
```
# 8. Create a serializers.py module
```py
# codigo_postal/serializer.py
from rest_framework import serializers
from .models import CodigoPostal
class CodigoPostalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CodigoPostal
        fields = '__all__' # Serialize all fields implicitly
```
# 8. Create a views.py module
```py
#codigo_postal/views.py:
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CodigoPostalSerializer
from .models import CodigoPostal
# ModelViewSet is a special view that Django Rest Framework provides.
# It will handle GET and POST for CodigoPostal without us having to do any more work.
class CodigoPostalViewSet(viewsets.ModelViewSet):
    queryset = CodigoPostal.objects.all().order_by('codigo')
    serializer_class = CodigoPostalSerializer
```
# 9. Wire these views up in urls.py module
```py
# codigo_postal/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'codigo_postal', views.CodigoPostalViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
```
and 
```py
# api_codigo_postal/urls.py
from django.contrib import admin
from django.urls import path,include # NEW

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('codigo_postal.urls')), # NEW
]
```
# 10. Test our Web API
```
python manage.py runserver
```