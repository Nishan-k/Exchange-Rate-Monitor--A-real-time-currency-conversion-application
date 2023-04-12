import pandas as pd
from kafka import KafkaProducer
import time

# Reading the data:
amazon = pd.read_csv("data/amazon.csv")
apple = pd.read_csv("data/apple.csv")
coke = pd.read_csv("data/coke.csv")
google = pd.read_csv("data/google.csv")
ibm = pd.read_csv("data/ibm.csv")
johnson = pd.read_csv("data/johnson.csv")
meta = pd.read_csv("data/meta.csv")
nvidia = pd.read_csv("data/nvidia.csv")
pinterest = pd.read_csv("data/pinterest.csv")
tesla = pd.read_csv("data/tesla.csv")

# Creating the Kafka Producer:
producer = KafkaProducer(bootstrap_servers ="localhost:9093", acks=1)
# producer.send("currency-topic", bytes(kafka_data, 'utf-8'))


for i in range(0, 5):
    amz_data = amazon.iloc[i].to_json()
    apple_data = apple.iloc[i].to_json()
    coke_data = coke.iloc[i].to_json()
    google_data = google.iloc[i].to_json()
    ibm_data = ibm.iloc[i].to_json()
    jandj_data = johnson.iloc[i].to_json()
    meta_data = meta.iloc[i].to_json()
    nvidia_data = nvidia.iloc[i].to_json()
    pinterest_data = pinterest.iloc[i].to_json()
    tesla_data = tesla.iloc[i].to_json()

    producer.send("amazon-topic", bytes(amz_data, "utf-8"))
    # producer.send("apple-topic", bytes(apple_data, "utf-8"))
    # producer.send("coke-topic", bytes(coke_data, "utf-8"))
    # producer.send("google-topic", bytes(google_data, "utf-8"))
    # producer.send("ibm-topic", bytes(ibm_data, "utf-8"))
    # producer.send("johnson-topic", bytes(jandj_data, "utf-8"))
    # producer.send("meta-topic", bytes(meta_data, "utf-8"))
    # producer.send("nvidia-topic", bytes(nvidia_data, "utf-8"))
    # producer.send("pinterest-topic", bytes(pinterest_data, "utf-8"))
    # producer.send("tesla-topic", bytes(tesla_data, "utf-8"))
    time.sleep(5)
