import json


def load_json_data(file_path):
    with open(
        file_path,
        encoding="utf-8"
    ) as file:
        return json.load(file)


def load_login_data():
    return load_json_data(
        "test_data/login_data.json"
    )


def load_alerts_data():
    return load_json_data(
        "test_data/alerts_data.json"
    )


def load_hover_data():
    return load_json_data(
        "test_data/hover_data.json"
    )
