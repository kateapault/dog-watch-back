from django.shortcuts import render
from .models import Dog, Food, Treat, Out, Walkie
from .serializers import DogSerializer
from rest_framework import generics

class DogListCreate(generics.ListCreateAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
    