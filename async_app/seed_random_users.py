"""This module directly call the create user API and insert the data."""
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed


API_URL = "http://127.0.0.1:8000/user/"


def parse_user(data):
    return {
        "uuid": data["login"]["uuid"],
        "username": data["login"]["username"],
        "password": data["login"]["password"],
        "email": data["email"],
        "first_name": data["name"]["first"],
        "last_name": data["name"]["last"],
        "city": data["location"]["city"],
        "state": data["location"]["state"],
        "country": data["location"]["country"],
        "phone": data["phone"],
        "dob": data["dob"]["date"]
    }


def post_user(user_payload):
    try:
        response = requests.post(API_URL, json=user_payload)
        return {
            "username": user_payload["username"],
            "status": response.status_code,
            "response": response.json()
        }
    except Exception as exc:
        return {
            "username": user_payload.get("username", "N/A"),
            "error": str(exc),
            "status": "error"
        }


def load_and_post_users_concurrently(n: int = 50, max_works: int = 10):
    response = requests.get(f"https://randomuser.me/api/?results={n}")
    if response.status_code != 200:
        return

    users = [
        parse_user(user) for user in response.json()["results"]
    ]

    with ThreadPoolExecutor(max_workers=max_works) as executor:
        futures = [executor.submit(post_user, user) for user in users]
        for future in as_completed(futures):
            result = future.result()
            print(result)


if __name__ == "__main__":
    load_and_post_users_concurrently(
        n=100,
        max_works=20
    )
