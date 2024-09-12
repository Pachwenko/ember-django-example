from api.tests.factories.rental import RentalFactory
from api.tests.factories.location import LocationFactory

from django.test import TestCase

class TestRentalModel(TestCase):

    def test_create_rental(self):
        location = LocationFactory()
        RentalFactory(
            description='a description',
            owner='a owner',
            city='a city',
            title='a title',
            category='House',
            image='link to a image',
            bedrooms=4,
            location=location
        )
