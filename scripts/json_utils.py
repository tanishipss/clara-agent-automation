import json


def safe_parse_json(text):

    try:
        return json.loads(text)
    except Exception:
        return {}