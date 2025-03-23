from django.shortcuts import get_object_or_404, _get_queryset
from django.contrib.auth.models import User
from rest_framework import status, generics
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
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

    def get_queryset(self):
        user = self.request.user
        return PolygonModel.objects.filter(users__id=user.id)

    def perform_create(self, serializer):
        if serializer.is_valid():
            try:
                serializer.save()
                # TODO polygon.users.add(self.request.user.id)
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
        return PolygonModel.objects.filter(users__id=self.request.user.id)
