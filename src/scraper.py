from google_play_scraper import Sort, reviews
import json
import os
from datetime import datetime

APP_ID = "com.zeptoconsumerapp"  # Zepto App ID

def fetch_reviews():
    print("Fetching Zepto reviews...")

    all_reviews = []
    next_token = None
    total_limit = 600  # Limited for performance + avoid blocking
    fetched = 0

    while fetched < total_limit:
        batch, next_token = reviews(
            APP_ID,
            lang="en",
            country="in",
            sort=Sort.NEWEST,
            count=200,
            continuation_token=next_token
        )

        if not batch:
            break

        for review in batch:
            review_date = review["at"]
            if review_date.year < 2024 or (review_date.year == 2024 and review_date.month < 6):
                next_token = None
                break

            all_reviews.append({
                "date": review_date.strftime("%Y-%m-%d"),
                "review": review["content"],
                "rating": review["score"]
            })

        fetched += len(batch)
        print(f"Fetched so far: {len(all_reviews)} reviews")

        if next_token is None:
            break

    os.makedirs("data", exist_ok=True)

    with open("data/raw_reviews.json", "w", encoding="utf-8") as f:
        json.dump(all_reviews, f, indent=4, ensure_ascii=False)

    print(f"\nDone! Total saved: {len(all_reviews)}")
    print("File created: data/raw_reviews.json")

if __name__ == "__main__":
    fetch_reviews()
