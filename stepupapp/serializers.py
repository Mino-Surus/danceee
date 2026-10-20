from rest_framework.serializers import ModelSerializer
from . import models

class NumberSerializers(ModelSerializer):
    class Meta:
        model = models.Number
        fields = ['value', 'name', 'founder']
# class DancebandSerializers(ModelSerializer):
#     class Meta:
#         model = models.Danceband
#         fields = ['name', 'country']

# class DancerSerialisers(ModelSerializer):
#     class Meta:
#         model = models.Dancer
#         fields = ['name', 'price', 'danceband']