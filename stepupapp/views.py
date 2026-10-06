from django.shortcuts import render
from .models import Danceband, Dancer
from rest_framework.viewsets import ModelViewSet
from .serializers import DancebandSerializers, DancerSerialisers
class DancebandViewSet(ModelViewSet):
    queryset = Danceband.objects.all()
    serializer_class = DancebandSerializers
class DancerViewSet(ModelViewSet):
    queryset = Dancer.objects.all()
    serializer_class = DancerSerialisers

