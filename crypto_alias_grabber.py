import json

import requests

url = "https://rest.coincap.io/v3/assets?ids="
headers = {
    "accept": "application/json",
    "Authorization": "Bearer a4060ca4aed5b1e6b169cb6a7d013622abb7fb4e8fe32229d77c16db8e5d1a6b",
}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()["data"]
    ids = [name["id"] for name in data]
    symbols = [short["symbol"] for short in data]

aliases = {symbol.lower(): coin_id for symbol, coin_id in zip(symbols, ids)}

with open("aliases.json", "w") as f:
    json.dump(aliases, f, indent=2)
