from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from . import models



class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Users
        fields = ('company_name','username', 'password')
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserRegistrationSerializer, self).create(validated_data)
    


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Devices
        fields = ('name','model')