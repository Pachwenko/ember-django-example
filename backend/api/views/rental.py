from rest_framework import viewsets

from api.serializers.rental import RentalSerializer
from api.models.rental import Rental


class RentalViewSet(viewsets.ModelViewSet):
    serializer_class = RentalSerializer
    queryset = Rental.objects.prefetch_related('location').all()
