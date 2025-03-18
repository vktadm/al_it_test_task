from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from .models import PolygonModel
from .serializers import PoligonModelSerializer


class PoligonViewSet(viewsets.ViewSet):
    """Представления для Polygon"""

    queryset = PolygonModel.objects.all()

    def list(self, request):
        """Получить все объекты."""
        serializer = PoligonModelSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Получить объект по id."""
        item = get_object_or_404(self.queryset, pk=pk)
        serializer = PoligonModelSerializer(item)
        return Response(serializer.data)
