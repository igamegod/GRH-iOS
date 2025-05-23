from mitmproxy import http
import json
import os

def load_json(filename):
    path = os.path.join(os.path.dirname(__file__), filename)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

inventory_json = load_json("inventory.json")
catalog_json = load_json("catalog.json")
buy_json = load_json("buy.json")

def response(flow: http.HTTPFlow) -> None:
    url = flow.request.pretty_url

    if url == "https://go.gunraidersapi.com/api/v32/inventory/all/0":
        flow.response.text = json.dumps(inventory_json)
        flow.response.headers["Content-Type"] = "application/json"
        
    elif url == "https://go.gunraidersapi.com/api/v32/store/catalog":
        flow.response.text = json.dumps(catalog_json)
        flow.response.headers["Content-Type"] = "application/json"

    elif url == "https://go.gunraidersapi.com/api/v32/inventory/buy":
        flow.response.text = json.dumps(buy_json)
        flow.response.headers["Content-Type"] = "application/json"