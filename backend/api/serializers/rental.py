from rest_framework_json_api import serializers

from api.models.rental import Rental
from api.serializers.location import LocationSerializer


class RentalSerializer(serializers.ModelSerializer):
    included_serializers = {
        'location': LocationSerializer,
    }

    class Meta:
        model = Rental
        fields = '__all__'

    class JSONAPIMeta:
        # When doing this make sure to add something for prefetching in the view
        # see https://django-rest-framework-json-api.readthedocs.io/en/stable/usage.html#performance-improvements
        included_resources = ['location']
