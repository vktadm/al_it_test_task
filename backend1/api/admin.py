from django.contrib import admin

from leaflet.admin import LeafletGeoAdmin
from .models import PolygonModel


@admin.register(PolygonModel)
class ShopAdmin(LeafletGeoAdmin):
    list_display = ("name", "poly", "antemeridian")
