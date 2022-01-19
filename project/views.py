from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *

class CarView(APIView):
    def get(self, request):
        query = CarModel.objects.all()
        serializer = CarSerializer(query, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CarUpdate(UpdateAPIView):
    serializer_class = CarSerializer

class CarDelete(DestroyAPIView):
    serializer_class = CarSerializer

class UserRegister(APIView):
    def post(self, request):
        post_data = request.data
        serializer = UserSerializer(data=post_data)
        if serializer.is_valid():
            serializers.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AppUserView(APIView):
    def get(self, request):
        query = AppUser.objects.all()
        serializer = AppUserSerializer(query, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = AppUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CityView(APIView):
    def get(self, request):
        query = CityModel.objects.all()
        serializer = CitySerializer(query, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)