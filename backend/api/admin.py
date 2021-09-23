from django.contrib import admin

from api.models.rental import Rental
from api.models.location import Location


admin.site.register(Rental)
admin.site.register(Location)