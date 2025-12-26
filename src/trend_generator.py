import pandas as pd
from datetime import datetime, timedelta
import os

def generate_trend():
    df = pd.read_json("data/topics.json")
    
    df["date"] = pd.to_datetime(df["date"])
    end_date = df["date"].max()
    start_date = end_date - timedelta(days=30)

    df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]

    trend = df.groupby(["topic", "date"]).size().unstack(fill_value=0)

    os.makedirs("output", exist_ok=True)
    trend.to_csv("output/trend_report.csv")

    print("Trend Report Generated ➜ output/trend_report.csv")

if __name__ == "__main__":
    generate_trend()
