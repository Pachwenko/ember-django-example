from rest_framework_json_api import serializers

from api.models.location import Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
