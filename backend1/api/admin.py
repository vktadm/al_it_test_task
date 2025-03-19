from django.contrib import admin

from leaflet.admin import LeafletGeoAdmin
from .models import PolygonModel, UserPolygon


@admin.register(PolygonModel)
class PolygonAdmin(LeafletGeoAdmin):
    list_display = ("name", "poly", "antemeridian")


admin.site.register(UserPolygon)
