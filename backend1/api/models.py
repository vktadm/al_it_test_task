from django.contrib.gis.db import models
from django.contrib.auth.models import AbstractUser


class PolygonModel(models.Model):
    """Модель полигона."""

    name = models.CharField(max_length=100)
    poly = models.PolygonField()
    antemeridian = models.BooleanField()
    users = models.ManyToManyField("UserModel", through="UserPolygonModel")

    class Meta:
        verbose_name = "Полигон"
        verbose_name_plural = "Полигоны"

    def __str__(self):
        return self.name


class UserModel(AbstractUser):
    polygons = models.ManyToManyField("PolygonModel", through="UserPolygonModel")


class UserPolygonModel(models.Model):
    """Промежуточную таблица для User и PolygonModel."""

    creator = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    polygon = models.ForeignKey(PolygonModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Полигон - Пользователь"
        verbose_name_plural = "Полигон - Пользователь"

    def __str__(self):
        """Строковое представление."""
        return f"{self.get_creator_name()} - {self.created_at}"

    def get_creator_name(self):
        return UserModel.objects.get(pk=self.creator.id)
