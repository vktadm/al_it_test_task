from django.shortcuts import get_object_or_404, _get_queryset
from django.contrib.auth.models import User
from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import UserModel, PolygonModel, UserPolygonModel
from .serializers import PolygonModelSerializer, UserSerializer


class CreateUserView(generics.CreateAPIView):
    queryset = _get_queryset(User)
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class PolygonListCreate(generics.ListCreateAPIView):
    serializer_class = PolygonModelSerializer
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]

    def get_queryset(self):
        user = self.request.user
        return PolygonModel.objects.filter(users__id=user.id)
        # return PolygonModel.objects.all()

    def perform_create(self, serializer):
        if serializer.is_valid():
            try:
                serializer.save(users__id=self.request.user.id)
            except Exception as e:
                return Response(f"ERROR: {e}", status=status.HTTP_400_BAD_REQUEST)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            f"ERROR: {serializer.errors}", status=status.HTTP_400_BAD_REQUEST
        )


class PolygonDelete(generics.DestroyAPIView):
    queryset = PolygonModel.objects.all()
    serializer_class = PolygonModelSerializer
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]

    def get_queryset(self):
        user = self.request.user
        return PolygonModel.objects.filter(users__id=user.id)


class PolygonView(generics.CreateAPIView):  # viewsets.ViewSet
    """Представление для PolygonModel"""

    queryset = _get_queryset(PolygonModel)

    def list(self, request):
        """Получить все объекты."""
        queryset = _get_queryset(PolygonModel)
        serializer = PolygonModelSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Получить объект по id."""
        item = get_object_or_404(PolygonModel, pk=pk)
        serializer = PolygonModelSerializer(item)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """Создать объект."""
        serializer = PolygonModelSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except Exception as e:
                return Response(f"ERROR: {e}", status=status.HTTP_400_BAD_REQUEST)

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
