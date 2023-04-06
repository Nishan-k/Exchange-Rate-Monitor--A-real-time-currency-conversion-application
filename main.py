import requests
import credentials

BASE_URL = "https://api.currencyfreaks.com/v2.0/rates/latest?"
API_KEY = credentials.key
# https://api.currencyfreaks.com/v2.0/rates/latest?apikey=179befac34da4043bd6f00b7e48b5753
response = requests.get(f"https://api.currencyfreaks.com/v2.0/rates/latest?apikey={API_KEY}")
print(response.status_code)