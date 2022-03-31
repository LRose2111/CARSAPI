from django.shortcuts import get_object_or_404
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

@api_view(['GET', 'PUT', 'DELETE'])
def car_detail(request, pk):
        car = get_object_or_404(Car, pk=pk)
        if request.method == 'GET':
            
            serializer = Carserializer(car);
            return Response(serializer.data)
        elif request.method == 'PUT':
            
            serializer = Carserializer(car, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        elif request.method == 'DELETE':
            car.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


