import pytest

from api.tests.factories.rental import RentalFactory
from api.tests.factories.location import LocationFactory


# potentially helpful fixtures provided by pytest-django
# https://pytest-django.readthedocs.io/en/latest/helpers.html#fixtures

@pytest.mark.django_db()
def test_create_rental():
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
