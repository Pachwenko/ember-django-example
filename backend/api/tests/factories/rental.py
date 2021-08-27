import factory  # https://github.com/FactoryBoy/factory_boy
from api.models.rental import Rental

class RentalFactory(factory.Factory):
    class Meta:
        model = Rental

    owner = factory.Faker('name')
    type = factory.Faker('word')
    city = factory.Faker('word')
    title = factory.Faker('word')
    category = factory.Faker('word')
    description = factory.Faker('paragraph')
    image = factory.Faker('image_url', width=600, height=600)
    bedrooms = factory.Faker('pyint')
    # TODO: add location