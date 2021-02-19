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