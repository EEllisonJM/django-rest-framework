from django.contrib import admin
from django.urls import path,include # NEW

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('codigo_postal.urls')), # NEW
]