import json

APPS = "apps.json"

CACHE = {"APPS": None}


def list_apps():
    if CACHE["APPS"] is None:
        with open(APPS, "r") as f:
            CACHE["APPS"] = json.load(f)
    return CACHE["APPS"]


def get_app(app_code: str):
    apps = [app for app in list_apps() if app["code"] == app_code]
    return apps[0] if len(apps) > 0 else None
