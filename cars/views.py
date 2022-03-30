from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Carserializer
from .models import Car
from cars import serializers

@api_view('GET')
def cars_list(request):
    cars = Car.objects.all()


    serializer = Carserializer(cars, many=True)

    

    return Response('ok')

