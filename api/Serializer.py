from dataclasses import field, fields
import email
from rest_framework import serializers
from api.models import user,Todo

class userserializers(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['email','phone']
class signupserialiser(serializers.ModelSerializer)  :
    class Meta:
        model = user 
        fields = [ 'email','phone','password'] 
class todoserializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
          