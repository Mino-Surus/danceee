from django.shortcuts import render
from .models import Number
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response 
from .serializers import NumberSerializers
from rest_framework.decorators import action
import random

class NumberViewSet(ModelViewSet):
    queryset = Number.objects.all()
    serializer_class = NumberSerializers

    @action(methods=['GET'], detail=False, url_path='random')
    def random_number(self, request):
        min_value = int(request.GET.get('min', 0))
        max_value = int(request.GET.get('max', 100))
        number = random.randint(min_value, max_value)
        return Response({'number': number})



