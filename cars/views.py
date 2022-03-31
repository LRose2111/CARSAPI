import re
from turtle import st
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import Carserializer
from .models import Car
from cars import serializers

@api_view(['GET', 'POST'])
def cars_list(request):
   

    if request.method == 'GET':
        cars = Car.objects.all()
        serializer = Carserializer(cars, many=True)
        return Response(serializer.data)


    elif request.method == 'POST':
        serializer = Carserializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

@api_view(['GET'])
def car_detail(request, pk):
    try:
        car = Car.objects.get(pk=pk)
        serializer = Carserializer(car);
        return Response(serializer.data)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
