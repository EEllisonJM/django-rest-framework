from django.contrib.auth.models import User, Group
from rest_framework import serializers

# Notice that we're using hyperlinked relations in this case
# with HyperlinkedModelSerializer. You can also use primary 
# key and various other relationships, but hyperlinking is 
# good RESTful design.

# Define some serializers that we'll use for our data representations.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Product
#         fields = ['url', 'name']