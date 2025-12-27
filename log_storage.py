import json
import os
from config import LOG_FILE_PATH

def save_all_logs(logs: list):
    os.makedirs(os.path.dirname(LOG_FILE_PATH), exist_ok=True)
    with open(LOG_FILE_PATH, "w") as f:
        json.dump(logs, f, indent=4)


def delete_log(index: int):
    logs = load_logs()
    if 0 <= index < len(logs):
        logs.pop(index)
        save_all_logs(logs)


def load_logs() -> list:
    """
    Loads existing secure logs from storage.
    """
    if not os.path.exists(LOG_FILE_PATH):
        return []

    with open(LOG_FILE_PATH, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def save_log(secure_log: dict) -> None:
    """
    Saves a secure log entry to storage.
    """
    logs = load_logs()
    logs.append(secure_log)

    with open(LOG_FILE_PATH, "w") as file:
        json.dump(logs, file, indent=4)
