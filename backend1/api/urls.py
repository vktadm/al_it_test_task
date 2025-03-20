from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CreateUserView, PolygonListCreate, PolygonDelete

# router = routers.DefaultRouter()
# router.register(r"polygon", PolygonView)

urlpatterns = [
    path("polygons/", PolygonListCreate.as_view(), name="polygon-list"),
    path("polygons/delete/<int:pk>/", PolygonDelete.as_view(), name="polygon-delete"),
    path("register/", CreateUserView.as_view(), name="register"),
    path("token/", TokenObtainPairView.as_view(), name="get_token"),
    path("token/refresh/", TokenRefreshView.as_view(), name="refresh_token"),
    path("", include("rest_framework.urls")),
    # path("", include(router.urls)),
]
