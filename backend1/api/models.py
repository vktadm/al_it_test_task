from django.contrib.gis.db import models


class PolygonModel(models.Model):
    """Модель полигона."""

    name = models.CharField(max_length=100)
    poly = models.PolygonField()
    antemeridian = models.BooleanField()

    def __str__(self):
        return self.name
