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