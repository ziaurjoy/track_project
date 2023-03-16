from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import status
import jwt
from track_project.settings import SIMPLE_JWT

from . import serializers
from . import models
from django.http import Http404



# Create your views here.


class UserRegistrationAPI(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]
    def post(self, request, format = None):
        data = request.data
        serializer = serializers.UserRegistrationSerializer(data= data)
        if serializer.is_valid():
            serializer.save()
            message = {'message': 'User Create Success'}
            return Response(message, status=status.HTTP_201_CREATED)
        else:
            message = {'message': 'Registration Failed'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)




class DeviceCreateListAPI(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]

    def post(self, request, format = None):
        token = request.headers['Authorization'][7:]
        token_decode = jwt.decode(token, SIMPLE_JWT['SIGNING_KEY'], algorithms=[SIMPLE_JWT['ALGORITHM']])
        user_id = token_decode['user_id']
        
        data = request.data
        serializer = serializers.DeviceSerializer(data= data)
        if serializer.is_valid():
            user = models.Users.objects.get(id = int(user_id))
            serializer.validated_data['user'] = user
            serializer.save()
            message = {'message': 'Device Create Success'}
            return Response(message, status=status.HTTP_201_CREATED)
        else:
            message = {'message': 'Device Create Failed'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format = None):
        token = request.headers['Authorization'][7:]
        token_decode = jwt.decode(token, SIMPLE_JWT['SIGNING_KEY'], algorithms=[SIMPLE_JWT['ALGORITHM']])
        user_id = token_decode['user_id']

        device = models.Devices.objects.filter(user__id = int(user_id))
        serializer = serializers.DeviceSerializer(device, many=True)
        return Response(serializer.data)



class DeviceDetail(APIView):
    """
    Retrieve, update or delete a device instance
    """
    def get_object(self, pk, user_id):
        # Returns an object instance that should 
        # be used for detail views.
        try:
            return models.Devices.objects.get(pk=pk, user__id = int(user_id))
        except models.Devices.DoesNotExist:
            raise Http404
  
    def get(self, request, pk, format=None):
        token = request.headers['Authorization'][7:]
        token_decode = jwt.decode(token, SIMPLE_JWT['SIGNING_KEY'], algorithms=[SIMPLE_JWT['ALGORITHM']])
        user_id = token_decode['user_id']

        device = self.get_object(pk, user_id)
        serializer = serializers.DeviceSerializer(device)
        return Response(serializer.data)
  
    def put(self, request, pk, format=None):
        token = request.headers['Authorization'][7:]
        token_decode = jwt.decode(token, SIMPLE_JWT['SIGNING_KEY'], algorithms=[SIMPLE_JWT['ALGORITHM']])
        user_id = token_decode['user_id']

        device = self.get_object(pk, user_id)
        serializer = serializers.DeviceSerializer(device, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
          
    def delete(self, request, pk, format=None):
        token = request.headers['Authorization'][7:]
        token_decode = jwt.decode(token, SIMPLE_JWT['SIGNING_KEY'], algorithms=[SIMPLE_JWT['ALGORITHM']])
        user_id = token_decode['user_id']
        device = self.get_object(pk, user_id)
        device.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)