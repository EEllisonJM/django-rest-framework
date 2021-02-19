# Quickstart
Simple API to allow admin users to view and edit the users and groups in the system.
## Project setup
### Create the project directory
```
mkdir tutorial
cd tutorial
```
### Create a virtual environment to isolate our package dependencies locally
```
python3 -m venv env
source env/bin/activate  
```
### On Windows use
```
env\Scripts\activate
```
### Install Django and Django REST framework into the virtual environment
```
pip install django
pip install djangorestframework
```
### Set up a new project with a single application
Note the trailing '.' character
```
django-admin startproject tutorial .  
cd tutorial
django-admin startapp quickstart
cd ..
```
### Now sync your database for the first time:
```
python manage.py migrate
```
### We'll also create an initial user named 'ellis' with a password of 'ellis'. We'll authenticate as that user later in our example.
```
python manage.py createsuperuser --email ellis@example.com --username ellis
```
## Run the Django server:
```
python manage.py runserver
```
## Serializers : Data representations.
```python
# tutorial/quickstart/serializers.py
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
```
## Views
### Viewsets keeps the view logic nicely organized as well as being very concise.
```py
# tutorial/quickstart/views.py 
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
```
## URLs : Wire up the API URLs.
```py
# tutorial/urls.py
from django.urls import include, path
from rest_framework import routers
from tutorial.quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
```
## Pagination : Control how many objects per page are returned.
```py
# tutorial/settings.py

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
```
## Settings : Module
Add 'rest_framework' to INSTALLED_APPS.
# tutorial/settings.py
```py
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```
## Run the Django server:
```
python manage.py runserver
```
## Testing our API
```
http -a admin:admin http://127.0.0.1:8000/users/
http -a ellis:ellis http://127.0.0.1:8000/users/
```
From : https://www.django-rest-framework.org/tutorial/quickstart/