from django.urls import include, path
from rest_framework import routers
from .views import PoligonViewSet

router = routers.DefaultRouter()
router.register(r"poligon", PoligonViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
