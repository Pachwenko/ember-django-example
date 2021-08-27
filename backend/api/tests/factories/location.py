import factory  # https://github.com/FactoryBoy/factory_boy
from api.models.location import Location

class LocationFactory(factory.Factory):
    class Meta:
        model = Location

    lat = factory.Faker('latitude')
    lng = factory.Faker('longitude')