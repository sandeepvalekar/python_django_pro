from rest_framework import serializers
from api.models import client ,project

class ClientSerializers(serializers.HyperlinkedModelSerializer):
   client_id=serializers.ReadOnlyField() 
   class Meta:
      model=client
      fields="__all__"

class projectSerializer(serializers.HyperlinkedModelSerializer):
   id=serializers.ReadOnlyField() 

   class Meta:
    model=project
    fields="__all__"