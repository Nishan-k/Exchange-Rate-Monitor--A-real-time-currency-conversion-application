import requests
import credentials
from kafka import KafkaProducer
import time

BASE_URL = "https://api.currencyfreaks.com/v2.0/rates/latest?"
API_KEY = credentials.key






i = 0
while i <= 4:
    response = requests.get(f"https://api.currencyfreaks.com/v2.0/rates/latest?apikey={API_KEY}")
    data = response.json()
    base = data['base']
    rates = {}
    currencies = data["rates"]
    for k,v in currencies.items():
        rates[k] = v

    kafka_data = {base:rates}
    producer = KafkaProducer(bootstrap_servers ="localhost:9093", acks=1)
    producer.send("currency-topic", bytes(kafka_data, 'utf-8'))
    time.sleep(12)
    i += 1
    producer.flush()