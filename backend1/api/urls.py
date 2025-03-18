from django.urls import include, path
from rest_framework import routers
from .views import Polygon

router = routers.DefaultRouter()
router.register(r"polygon", Polygon)

urlpatterns = [
    path("", include(router.urls)),
]
