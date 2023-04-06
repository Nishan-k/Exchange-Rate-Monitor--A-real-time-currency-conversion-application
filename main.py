import requests
import credentials
from kafka import KafkaProducer


BASE_URL = "https://api.currencyfreaks.com/v2.0/rates/latest?"
API_KEY = credentials.key
response = requests.get(f"https://api.currencyfreaks.com/v2.0/rates/latest?apikey={API_KEY}")



data = response.json()
base = data['base']
rates = {}
currencies = data["rates"]
for k,v in currencies.items():
    rates[k] = v

producer = KafkaProducer(bootstrap_servers ="localhost:9093", acks=1)
producer.send("currency-topic", bytes(base, 'utf-8'))
producer.flush()