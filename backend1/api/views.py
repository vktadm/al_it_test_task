from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404, _get_queryset
from rest_framework.response import Response

from .models import PolygonModel
from .serializers import PoligonModelSerializer


class Polygon(viewsets.ViewSet):
    """Представление для PolygonModel"""

    queryset = _get_queryset(PolygonModel)

    def list(self, request):
        """Получить все объекты."""
        queryset = _get_queryset(PolygonModel)
        serializer = PoligonModelSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Получить объект по id."""
        item = get_object_or_404(PolygonModel, pk=pk)
        serializer = PoligonModelSerializer(item)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """Создать объект."""
        serializer = PoligonModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """Удалить объект."""
        item = get_object_or_404(self.queryset, pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, pk=None):
        # TODO
        pass
