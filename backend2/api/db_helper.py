from django.db import connection
from django.contrib.gis.geos import Polygon


def sql_qwery(polygon: str) -> list[dict] | None:
    try:
        polygon = Polygon()
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(
        """SELECT 
                id, 
                name, 
                ST_AsGeoJSON(
                    ST_Intersection(
                        poly, %s::geometry
                    )
                ) AS intersection
                FROM api_polygonmodel as p
                WHERE ST_Intersects(
                    poly, %s::geometry
                );""",
        [polygon, polygon],
    )
    result = cursor.fetchall()
    return result


# poly = "SRID=4326; POLYGON ((28 53, 31 53, 30 52, 28 52, 28 53))"
# print(poly)
#
# print(sql_qwery(poly))
