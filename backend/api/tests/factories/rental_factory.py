import factory  # https://github.com/FactoryBoy/factory_boy
from api.models.rental import Rental

class RentalFactory(factory.Factory):
    class Meta:
        model = Rental
    description = factory.Faker('paragraph')