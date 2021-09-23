from decimal import Decimal
import pytest

from api.tests.factories.location import LocationFactory


# potentially helpful fixtures provided by pytest-django
# https://pytest-django.readthedocs.io/en/latest/helpers.html#fixtures

@pytest.mark.django_db()
def test_create_rental():
    LocationFactory(
        lat=Decimal(20.123456789),
        lng=Decimal(20.123456789),
    )
