import pandas_datareader.data as web
import pandas as pd
import datetime
import os

def get_stock_data():

    os.makedirs("data", exist_ok=True)

    start = datetime.datetime(2022, 1, 1)
    end = datetime.datetime(2024, 1, 1)

    stock = web.DataReader("AAPL", "stooq", start, end)

    stock.reset_index(inplace=True)

    stock.to_csv("data/stock_data.csv", index=False)

    print("Stock data saved successfully!")

if __name__ == "__main__":
    get_stock_data()