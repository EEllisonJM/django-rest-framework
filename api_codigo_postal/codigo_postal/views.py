#codigo_postal/views.py:
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CodigoPostalSerializer
from .models import CodigoPostal
from rest_framework import generics
# ModelViewSet is a special view that Django Rest Framework provides.
# It will handle GET and POST for CodigoPostal without us having to do any more work.
class CodigoPostalViewSet(viewsets.ModelViewSet):
    queryset = CodigoPostal.objects.all().order_by('codigo')
    serializer_class = CodigoPostalSerializer

    # def getByCodigoBarra:
    #     wild_books = Book.objects.filter(title__contains='wild')