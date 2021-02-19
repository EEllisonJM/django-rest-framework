# myapi/serializers.py
from rest_framework import serializers

from .models import Hero

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        #fields = ('name', 'alias') # Serialize fields explicitly
        fields = '__all__' # Serialize all fields implicitly
        