from rest_framework import serializers

from .models import PolygonModel, UserModel


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


class PolygonModelSerializer(serializers.ModelSerializer):
    """Сериализатор для модели PolygonModel."""

    # poly = serializers.SerializerMethodField()

    class Meta:
        model = PolygonModel
        fields = ("id", "name", "poly", "antemeridian", "users")

    # def get_poly(self, obj):
    #     return f"{obj.poly[0][0:4]}"
