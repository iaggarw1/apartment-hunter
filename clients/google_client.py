import requests

# curl -X POST -d '{
#  "includedTypes": ["restaurant"],
#  "maxResultCount": 10,
#  "locationRestriction": {
#    "circle": {
#      "center": {
#        "latitude": 37.7937,
#        "longitude": -122.3965},
#      "radius": 500.0
#    }
#  }
# }' \
# -H 'Content-Type: application/json' -H "X-Goog-Api-Key: API_KEY" \
# -H "X-Goog-FieldMask: places.displayName" \
# https://places.googleapis.com/v1/places:searchNearby

DOMAIN = 'https://places.googleapis.com/'


def search_nearby(query: dict, config: dict):
    # includedTypes must be a list of strings (Table A). Normalize if a single str slipped in.
    inc = config["includedType"]
    if isinstance(inc, str):
        included_types = [inc]
    else:
        included_types = [str(x) for x in inc if x]

    max_result_count = min(max(1, int(config["results"])), 20)

    payload = {
        "includedTypes": included_types,
        "maxResultCount": max_result_count,
        "locationRestriction": {
            "circle": {
                "center": {
                    "latitude": float(query["latitude"]),
                    "longitude": float(query["longitude"]),
                },
                "radius": float(query["radius"]),
            }
        },
    }
    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": query["secret"],
        "X-Goog-FieldMask": "places.id,places.displayName,places.types,places.location",
    }
    url = DOMAIN + "v1/places:searchNearby"
    r = requests.post(url, json=payload, headers=headers, timeout=30)

    if not r.ok:
        return {
            "error": True,
            "status_code": r.status_code,
            "body": r.text,
            "hint": "Check longitude (west = negative, e.g. SF -122.4) and radius in meters (try 500–5000).",
        }

    try:
        data = r.json()
    except requests.JSONDecodeError:
        return {"error": True, "body": r.text}

    if not (data.get("places") or []) and not data.get("error"):
        data["_hint"] = (
            "No places in circle. Use negative longitude for US west coast; "
            "radius is in meters—20m is very small; try 1500+."
        )
    return data