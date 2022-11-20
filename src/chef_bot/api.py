import requests
import json
from environs import Env

# Read .env file and set environment variables.
env = Env()
env.read_env()


def get_nutrients(food: str) -> dict[str, any]:
    url = "https://trackapi.nutritionix.com/v2/natural/nutrients"

    payload = json.dumps(
        {
            "query": food,
            "line_delimited": True,
            "use_raw_foods": True,
            "use_branded_foods": False,
        }
    )
    headers = {
        "x-app-id": env("NUTRITIONIX_APPLICATION_ID"),
        "x-app-key": env("NUTRITIONIX_API_KEY"),
        "x-remote-user-id": env("NUTRITIONIX_API_KEY"),
        "Content-Type": "application/json",
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()
