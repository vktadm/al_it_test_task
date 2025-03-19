from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .db_helper import sql_qwery


@api_view(["GET"])
def check_polygon(request, polygon: str):
    polygons = sql_qwery(polygon)
    if polygons:
        return Response({"message:": f"{polygons}"})
    return Response({"message:": f"No content"}, status=status.HTTP_204_NO_CONTENT)
