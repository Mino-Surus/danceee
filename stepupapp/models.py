from django.db import models

class Danceband(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField()

class Dancer(models.Model):
    name = models.CharField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    danceband = models.ForeignKey (Danceband, on_delete=models.CASCADE)