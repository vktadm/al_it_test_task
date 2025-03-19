from django.urls import path, include
from rest_framework import routers

from .views import check_polygon

urlpatterns = [path("", check_polygon)]
