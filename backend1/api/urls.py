from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import PolygonView, CreateUserView

# router = routers.DefaultRouter()
# router.register(r"polygon", PolygonView)

urlpatterns = [
    path("polygon/", PolygonView.as_view(), name="polygon"),
    path("user/register/", CreateUserView.as_view(), name="register"),
    path("token/", CreateUserView.as_view(), name="get_token"),
    path("refresh/", TokenObtainPairView.as_view(), name="refresh_token"),
    path("auth/", include("rest_framework.urls")),
    # path("", include(router.urls)),
]
