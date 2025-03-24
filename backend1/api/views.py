from django.shortcuts import _get_queryset
from django.contrib.auth.models import User
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import PolygonModel
from .serializers import PolygonModelSerializer, UserSerializer

from .dependencies import check_polygon


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
                # check_polygon(serializer.data)
                serializer.save()
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
