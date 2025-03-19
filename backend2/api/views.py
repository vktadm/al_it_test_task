from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .db_helper import sql_qwery


@api_view(["GET"])
def check_polygon(request):
    """Находит координаты пересечения с существующими полигонами."""
    if request.data:
        try:
            polygons = sql_qwery(request.data["polygon"])
        except Exception as e:
            return Response(data=f"ERROR: {e}", status=status.HTTP_400_BAD_REQUEST)

        return Response(data=polygons)

    return Response(data=False)
