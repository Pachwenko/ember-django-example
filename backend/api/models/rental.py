from django.db import models
from django.db.models.fields.related import OneToOneField

from api.models.location import Location


class Rental(models.Model):
    STANDALONE = 'Standalone'
    COMMUNITY = 'Community'
    CATEGORY_CHOICES = [
        (STANDALONE, 'Standalone'),
        (COMMUNITY, 'Community')
    ]

    owner = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES)
    description = models.TextField()
    image = models.TextField()
    bedrooms = models.IntegerField(default=1)
    location = OneToOneField(Location, on_delete=models.CASCADE)
