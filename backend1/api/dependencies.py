import requests
from environs import Env


def check_polygon(polygon):
    env = Env()
    env.read_env()
    try:
        response = requests.get(env("BACKEND2_URL"))
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
    except requests.exceptions.HTTPError as http_err:
        print(f"ERROR: HTTP error occurred - {http_err}")
    except Exception as err:
        print(f"ERROR: {err}")

    return True
