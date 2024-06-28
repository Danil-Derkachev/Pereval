from django.db import models


class Coordinates(models.Model):
    latitude = models.FloatField(max_length=254)
    longitude = models.FloatField(max_length=254)
    height = models.IntegerField()
