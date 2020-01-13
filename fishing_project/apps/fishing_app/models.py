from django.db import models

class FishingPlace(models.Model):
     name = models.CharField('Name of place', max_length=100)
     lant = models.DecimalField(max_digits=10, decimal_places=8)
     long = models.DecimalField(max_digits=10, decimal_places=8)
     description = models.TextField('Description of place')
     photos = models.TextField('Photos of place')

class PlaceOrder(models.Model):
    FishingPlace = models

