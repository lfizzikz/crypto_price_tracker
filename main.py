import csv
import json
from datetime import datetime

import requests
from rich.console import Console
from rich.table import Table

with open("aliases.json", "r") as f:
    aliases = json.load(f)
raw_input = input("Enter the coins you want: ")
coins = []
if raw_input == "":
    raw_input = "btc, eth"
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
        rank = item["rank"]
        # print(
        #     f"{item["symbol"]} - ${rate:,.2f} | 24h Change: {assets}% | Rank: {rank}\n"
        # )
else:
    print("nothing found", response.status_code)

with open("prices.csv", "a", newline="") as f:
    writer = csv.writer(f)
    for item in data_assets["data"]:
        rate = round(float(item["priceUsd"]), 2)
        writer.writerow([datetime.now(), item["id"], f"{rate:,.2f}"])

table = Table(title="Crypto Prices")

table.add_column("Symbol")
table.add_column("Price")
table.add_column("24h Change")

for item in data_assets["data"]:
    table.add_row(item["symbol"], f"${rate:,.2f}", f"{assets}%")

Console().print(table)
