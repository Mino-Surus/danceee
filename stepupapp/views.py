from django.shortcuts import render
from .models import Danceband, Dancer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response 
from .serializers import DancebandSerializers, DancerSerialisers
from rest_framework.decorators import action
class DancebandViewSet(ModelViewSet):
    queryset = Danceband.objects.all()
    serializer_class = DancebandSerializers

    @action(methods=['GET'], detail=False, url_path='usa')
    def usa_dancebands_list(self, request):
        queryset = self.get_queryset().filter(country='USA')    
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
class DancerViewSet(ModelViewSet):
    queryset = Dancer.objects.all()
    serializer_class = DancerSerialisers


