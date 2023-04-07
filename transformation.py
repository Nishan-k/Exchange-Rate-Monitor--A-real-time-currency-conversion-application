import pandas as pd

def add_ticker(path, ticker):
    df = pd.read_csv(f"{path}")
    df['Stock'] = ticker
    print(df.head())
    df.to_csv(f"{path}")

add_ticker(path="data/amazon.csv", ticker="AMZN")
add_ticker(path="data/apple.csv", ticker="AAPL")
add_ticker(path="data/coke.csv", ticker="COKE")
add_ticker(path="data/google.csv", ticker="GOOG")
add_ticker(path="data/ibm.csv", ticker="IBM")
add_ticker(path="data/johnson.csv", ticker="JNJ")
add_ticker(path="data/meta.csv", ticker="META")
add_ticker(path="data/nvidia.csv", ticker="NVDA")
add_ticker(path="data/pinterest.csv", ticker="PINS")
add_ticker(path="data/tesla.csv", ticker="TSLA")