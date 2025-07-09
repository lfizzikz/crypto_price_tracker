import json

import requests

with open("aliases.json", "r") as f:
    aliases = json.load(f)
raw_input = input("Enter the coins you want: ")
coins = []
for coin in raw_input.lower().replace(" ", "").split(","):
    full_name = aliases.get(coin, coin)
    coins.append(full_name)

coins_list = ",".join(coins)
url = f"https://rest.coincap.io/v3/assets?ids={coins_list}"
headers = {
    "accept": "application/json",
    "Authorization": "Bearer a4060ca4aed5b1e6b169cb6a7d013622abb7fb4e8fe32229d77c16db8e5d1a6b",
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data_assets = response.json()
    for item in data_assets["data"]:
        rate = round(float(item["priceUsd"]), 2)
        assets = round(float(item["changePercent24Hr"]), 2)
        print(f"{item["symbol"]} - ${rate:,.2f} | 24h Change: {assets}%\n")
else:
    print("nothing found", response.status_code)
