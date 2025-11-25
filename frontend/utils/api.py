import requests

BASE_URL = "http://127.0.0.1:8000"

def generate_plan(data: dict):
    response = requests.post(f"{BASE_URL}/generate-plan", json=data)
    if response.status_code != 200:
        return {"error": "Something went wrong"}
    return response.json()
