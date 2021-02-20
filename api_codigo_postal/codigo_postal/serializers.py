# codigo_postal/serializer.py
from rest_framework import serializers
from .models import CodigoPostal
class CodigoPostalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CodigoPostal
        fields = '__all__' # Serialize all fields implicitly