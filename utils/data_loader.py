import json


def load_login_data():
    with open(
        "test_data/login_data.json",
        encoding="utf-8"
    ) as file:
        return json.load(file)