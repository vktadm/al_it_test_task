from django.db import connection


def sql_qwery(polygon):
    cursor = connection.cursor()
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
