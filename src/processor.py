import json
import pandas as pd
import re

def clean_text(text):
    text = re.sub(r"[^A-Za-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text.lower()

def process_reviews():
    df = pd.read_json("data/raw_reviews.json")
    df["cleaned"] = df["review"].apply(clean_text)
    df.to_json("data/cleaned_reviews.json", orient="records", indent=4)
    print("Processed reviews saved to data/cleaned_reviews.json")

if __name__ == "__main__":
    process_reviews()
