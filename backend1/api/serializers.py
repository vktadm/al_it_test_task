from rest_framework import serializers
from rest_framework_gis.serializers import GeoModelSerializer

from .models import PolygonModel, UserModel, UserPolygonModel


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели User."""

    class Meta:
        model = UserModel
        fields = ["id", "username", "password"]
        extra_kwargs = {
            "password": {"write_only": True},  # Поле не отображается при чтении
        }

    def create(self, validated_data):
        user = UserModel.objects.create_user(**validated_data)
        return user


class PolygonModelSerializer(GeoModelSerializer):
    """Сериализатор для модели PolygonModel."""

    class Meta:
        model = PolygonModel
        geo_field = "poly"
        fields = ("id", "name", "poly", "antemeridian", "users")
