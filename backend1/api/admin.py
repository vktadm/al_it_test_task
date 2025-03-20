from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from leaflet.admin import LeafletGeoAdmin
from .models import UserModel, PolygonModel, UserPolygonModel


@admin.register(PolygonModel)
class PolygonAdmin(LeafletGeoAdmin):
    list_display = ("name", "poly", "antemeridian")


admin.site.register(UserPolygonModel)
admin.site.register(UserModel, UserAdmin)
