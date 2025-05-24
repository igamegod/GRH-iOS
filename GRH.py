import requests
import mitmproxy.http
import json

def load_json_from_github(url):
    response = requests.get(url)
    return response.json()

inventory_url = "https://raw.githubusercontent.com/igamegod/GRH-iOS/main/inventory.json"
catalog_url = "https://raw.githubusercontent.com/igamegod/GRH-iOS/main/catalog.json"
buy_url = "https://raw.githubusercontent.com/igamegod/GRH-iOS/main/buy.json"

inventory_json = load_json_from_github(inventory_url)
catalog_json = load_json_from_github(catalog_url)
buy_json = load_json_from_github(buy_url)

def response(flow: mitmproxy.http.HTTPFlow) -> None:
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
