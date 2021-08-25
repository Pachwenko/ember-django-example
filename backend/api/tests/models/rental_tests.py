import pytest

from api.tests.factories.rental_factory import RentalFactory

# potentially helpful fixtures provided by pytest-django
# https://pytest-django.readthedocs.io/en/latest/helpers.html#fixtures

@pytest.mark.django_db()
def test_create_rental():
    RentalFactory(description='a description')