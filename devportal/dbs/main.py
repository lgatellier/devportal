# Should be a VMware vSphere plugin
import json

DBS = "dbs.json"

CACHE = {
    'DBS': None
}

def list_dbs(app_code: str = None):
    if not CACHE["DBS"]:
        with open(DBS, "r") as f:
            CACHE["DBS"] = json.load(f)

    if not app_code:
        return CACHE["DBS"]
    
    return CACHE["DBS"][app_code] if app_code in CACHE["DBS"] else None