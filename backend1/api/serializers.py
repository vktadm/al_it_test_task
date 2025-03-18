from rest_framework import serializers

from .models import PolygonModel


class PoligonModelSerializer(serializers.ModelSerializer):
    """Сериализатор для модели PolygonModel."""

    # poly = serializers.SerializerMethodField()

    class Meta:
        model = PolygonModel
        fields = ("id", "name", "poly", "antemeridian")

    # def get_poly(self, obj):
    #     return f"{obj.poly[0][0:4]}"
