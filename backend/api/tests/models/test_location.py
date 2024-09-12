from decimal import Decimal

from api.tests.factories.location import LocationFactory

from django.test import TestCase

class TestLocationModel(TestCase):

    def test_create_location(self):
        LocationFactory(
            lat=Decimal(20.123456789),
            lng=Decimal(20.123456789),
        )
