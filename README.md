# Zepto AI Agent – Trend Analysis on Google Play Reviews
**Author:** Harshadip Bal  
**Role Applied:** Pulsegen.io – AI Agent | Trend Analysis Assignment  
**Submission Date:** 26 December 2025  

---

## 📍 Project Overview
This project analyzes **Google Play Store reviews** of the **Zepto** app using an **AI-driven Agentic Architecture**.  
The objective is to identify key customer issues, feedback, and feature requests and track their **trends over the last 30 days**.

---

## 🎯 Key Features (As per assignment instructions)

| Requirement | Status |
|------------|--------|
| Reviews from Google Play Store | ✔️ Done |
| Time Range – June 2024 → Today | ✔️ Filter applied |
| Daily data batch processing | ✔️ Date based grouping |
| AI Agent for topic detection | ✔️ SentenceTransformer + Clustering |
| Classic topic modeling (LDA) avoided | ✔️ Not used |
| Trend report from T → T-30 | ✔️ Generated: output/trend_report.csv |
| Individual submission | ✔️ Unique implementation |

---

## 🧠 Agentic AI Architecture
1️⃣ **Scraper** – Collects reviews  
2️⃣ **Processor** – Cleans text  
3️⃣ **Embeddings Generator** – Converts text to vectors  
4️⃣ **Clusterer** – Groups similar issues into topics  
5️⃣ **Trend Analyzer** – Tracks topic frequency over 30 days  

> The AI agent automatically discovers new themes & avoids manual labeling.

---

## 🗂 Folder Structure

zepto-trend-analysis/
│
├─ data/
│ ├─ raw_reviews.json
│ ├─ cleaned_reviews.json
│ ├─ topics.json
│
├─ output/
│ ├─ trend_report.csv
│
├─ src/
│ ├─ scraper.py
│ ├─ processor.py
│ ├─ ai_agent.py
│ ├─ trend_generator.py
│
├─ requirements.txt
├─ README.md

yaml
Copy code

---

## ⚙️ How to Run

```bash
pip install -r requirements.txt
python src/scraper.py
python src/processor.py
python src/ai_agent.py
python src/trend_generator.py

## 🎥 Demo Video Link

🔗 https://drive.google.com/file/d/1Okkvk2qPzySPPoRbomvt9KGIZCZsMc4Z/view?usp=sharing
