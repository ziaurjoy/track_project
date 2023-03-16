
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import status
import jwt
from track_project.settings import SIMPLE_JWT

from django.http import Http404
from . import serializers
from . import models

# Create your views here.

#==============================================================================
# retun user id
def get_user(request):
    token = request.headers['Authorization'][7:]
    token_decode = jwt.decode(token, SIMPLE_JWT['SIGNING_KEY'], algorithms=[SIMPLE_JWT['ALGORITHM']])
    user_id = token_decode['user_id']
    return int(user_id)




#==============================================================================
# any company registration and use the app
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




#==============================================================================
# Add and get all device like that phone, laptop, tab etc
class DeviceCreateListAPI(APIView):
    def post(self, request, format = None):
        user_id = get_user(self.request)
        
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
        user_id = get_user(self.request)

        device = models.Devices.objects.filter(user__id = int(user_id))
        serializer = serializers.DeviceSerializer(device, many=True)
        return Response(serializer.data)



#==============================================================================
# get single device and operation update, delete
class DeviceDetailAPI(APIView):
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
        user_id = get_user(self.request)

        device = self.get_object(pk, user_id)
        serializer = serializers.DeviceSerializer(device)
        return Response(serializer.data)
  
    def put(self, request, pk, format=None):
        user_id = get_user(self.request)

        device = self.get_object(pk, user_id)
        serializer = serializers.DeviceSerializer(device, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
          
    def delete(self, request, pk, format=None):
        user_id = get_user(self.request)
        device = self.get_object(pk, user_id)
        device.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    



#==============================================================================
# Add Employee
class EmployeeCreateListAPI(APIView):
    def post(self, request, format = None):
        user_id = get_user(self.request)
        data = request.data
        serializer = serializers.EmployeeSerializer(data= data)
        if serializer.is_valid():
            user = models.Users.objects.get(id = int(user_id))
            serializer.validated_data['user'] = user
            serializer.save()
            message = {'message': 'Employee Create Success'}
            return Response(message, status=status.HTTP_201_CREATED)
        else:
            message = {'message': 'Employee Create Failed'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format = None):
        user_id = get_user(self.request)
        employee = models.Employees.objects.filter(user__id = int(user_id))
        serializer = serializers.EmployeeSerializer(employee, many=True)
        return Response(serializer.data)
    



#==============================================================================
# employee get single object update delete
class EmployeeDetailAPI(APIView):
    """
    Retrieve, update or delete a Employee instance
    """
    def get_object(self, pk, user_id):
        # Returns an object instance that should 
        # be used for detail views.
        try:
            return models.Employees.objects.get(pk=pk, user__id = int(user_id))
        except models.Employees.DoesNotExist:
            raise Http404
  
    def get(self, request, pk, format=None):
        user_id = get_user(self.request)

        employee = self.get_object(pk, user_id)
        serializer = serializers.EmployeeSerializer(employee)
        return Response(serializer.data)
  
    def put(self, request, pk, format=None):
        user_id = get_user(self.request)

        employee = self.get_object(pk, user_id)
        serializer = serializers.EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
          
    def delete(self, request, pk, format=None):
        user_id = get_user(self.request)
        employee = self.get_object(pk, user_id)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    



#==============================================================================
# Track Object Create
class TrackCreateListAPI(APIView):
    def post(self, request, format = None):
        user_id = get_user(self.request)
        
        data = request.data
        serializer = serializers.TrackSerializer(data= data)
        if serializer.is_valid():
            user = models.Users.objects.get(id = int(user_id))
            serializer.validated_data['user'] = user
            serializer.save()
            message = {'message': 'Track Create Success'}
            return Response(message, status=status.HTTP_201_CREATED)
        else:
            message = {'message': 'Track Create Failed'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format = None):
        user_id = get_user(self.request)

        track = models.Tracks.objects.filter(user__id = int(user_id))
        serializer = serializers.TrackSerializer(track, many=True)
        return Response(serializer.data)
    



#==============================================================================
# get Track single Object update delete
class TrackDetailAPI(APIView):
    """
    Retrieve, update or delete a Track instance
    """
    def get_object(self, pk, user_id):
        # Returns an object instance that should 
        # be used for detail views.
        try:
            return models.Tracks.objects.get(pk=pk, user__id = int(user_id))
        except models.Tracks.DoesNotExist:
            raise Http404
  
    def get(self, request, pk, format=None):
        user_id = get_user(self.request)

        track = self.get_object(pk, user_id)
        serializer = serializers.TrackSerializer(track)
        return Response(serializer.data)
  
    def put(self, request, pk, format=None):
        user_id = get_user(self.request)

        track = self.get_object(pk, user_id)
        serializer = serializers.TrackSerializer(track, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
          
    def delete(self, request, pk, format=None):
        user_id = get_user(self.request)
        track = self.get_object(pk, user_id)
        track.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
