from decimal import Decimal
import factory  # https://github.com/FactoryBoy/factory_boy

from api.models.location import Location


class LocationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Location

    lat = Decimal(41.480438)
    lng = Decimal(-91.576313)
