# Should be a VMware vSphere plugin
import json

VMS = "vms.json"

CACHE = {"VMS": None}


def list_vms(app_code: str = None):
    if not CACHE["VMS"]:
        with open(VMS, "r") as f:
            CACHE["VMS"] = json.load(f)

    if not app_code:
        return CACHE["VMS"]

    return CACHE["VMS"][app_code] if app_code in CACHE["VMS"] else None
