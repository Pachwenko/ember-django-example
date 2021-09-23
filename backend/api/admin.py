from django.contrib import admin

from api.models.rental import Rental
from api.models.location import Location


class RentalAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'category', 'bedrooms')
    list_filter = ('category', 'city')


class LocationAdmin(admin.ModelAdmin):
    list_display = ('lat', 'lng')


admin.site.register(Rental, RentalAdmin)
admin.site.register(Location, LocationAdmin)
