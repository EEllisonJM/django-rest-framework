# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views

#  La notación views.CodigoPostlViewSer indica la clase a usar 
# CodigoPostalViewSet y se puede encontrar en un módulo llamado views
# (es decir, dentro del fichero llamado views.py).
router = routers.DefaultRouter()
router.register(r'codigo_postal', views.CodigoPostalViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]