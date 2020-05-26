from rest_framework import serializers
from .models import Dog, Food, Treat, Out, Walkie

class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ('id', 'name', 'breed')