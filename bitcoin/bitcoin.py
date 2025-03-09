import json
import requests
import sys

if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")
try:
    sys.argv[1] = float(sys.argv[1])
except:
    sys.exit("Command-line argument is not a number")

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

o = response.json()
price = o["bpi"]["USD"]["rate_float"]
amount = price * sys.argv[1]
print(f"${amount:,.4f}")


