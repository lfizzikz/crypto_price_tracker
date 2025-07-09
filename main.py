import requests

coins = input("Enter the coins you want: ")
url_assets = f"https://rest.coincap.io/v3/assets?ids={coins}"
headers = {
    "accept": "application/json",
    "Authorization": "Bearer a4060ca4aed5b1e6b169cb6a7d013622abb7fb4e8fe32229d77c16db8e5d1a6b",
}

response_assets = requests.get(url_assets, headers=headers)

if response_assets.status_code == 200:
    data_assets = response_assets.json()
    for item in data_assets["data"]:
        rate = round(float(item["priceUsd"]), 2)
        assets = round(float(item["changePercent24Hr"]), 2)
        print(f"{item["symbol"]} - ${rate:,.2f} | 24h Change: {assets}%\n")
else:
    print("nothing found", response_assets.status_code)
