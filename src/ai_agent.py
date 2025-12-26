import json
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
import numpy as np

def label_cluster(texts, labels):
    topic_map = {}
    for label, text in zip(labels, texts):
        topic_map.setdefault(label, []).append(text)

    return [" ".join(topic_map[l][0].split()[:3]) for l in labels]

def extract_topics():
    df = pd.read_json("data/cleaned_reviews.json")
    texts = df["cleaned"].tolist()

    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(texts)

    n_topics = min(10, len(texts) // 15) or 3
    kmeans = KMeans(n_clusters=n_topics, random_state=42)
    kmeans.fit(embeddings)

    topics = label_cluster(texts, kmeans.labels_)
    df["topic"] = topics

    df.to_json("data/topics.json", indent=4, orient="records")
    print("Topics extracted -> data/topics.json")

if __name__ == "__main__":
    extract_topics()
