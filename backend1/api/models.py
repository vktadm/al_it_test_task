from django.contrib.gis.db import models
from django.contrib.auth.models import User


class PolygonModel(models.Model):
    """Модель полигона."""

    name = models.CharField(max_length=100)
    poly = models.PolygonField()
    antemeridian = models.BooleanField()

    class Meta:
        verbose_name = "Полигон"
        verbose_name_plural = "Полигоны"

    def __str__(self):
        return self.name


class UserPolygon(models.Model):
    """Промежуточную таблица для User и PolygonModel."""

    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    polygon = models.ForeignKey(PolygonModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Полигон - Пользователь"
        verbose_name_plural = "Полигон - Пользователь"

    def __str__(self):
        """Строковое представление."""
        return f"{self.get_creator_name()} - {self.created_at}"

    def get_creator_name(self):
        return User.objects.get(pk=self.creator.id)
