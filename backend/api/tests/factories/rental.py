import factory  # https://github.com/FactoryBoy/factory_boy
import factory.fuzzy
from api.models.rental import Rental

from api.tests.factories.location import LocationFactory


class RentalFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Rental

    owner = factory.Faker('name')
    city = factory.Faker('word')
    title = factory.Faker('word')
    category = factory.fuzzy.FuzzyChoice([x[0] for x in Rental.CATEGORY_CHOICES])
    description = factory.Faker('paragraph')
    image = factory.Faker('image_url', width=600, height=600)
    bedrooms = factory.Faker('pyint')
    location = factory.SubFactory(LocationFactory)
