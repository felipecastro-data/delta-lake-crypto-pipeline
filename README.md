# 🚀 Delta Lake Crypto Pipeline

This PySpark project builds a modern Delta Lake pipeline to ingest cryptocurrency data from the CoinGecko API, clean and transform it using Apache Spark, and store it in Delta format using Microsoft Fabric.

---

## 📌 Problem Statement

Real-time crypto data is highly valuable for traders and analysts, but handling large volumes of time-series data efficiently requires scalable pipelines. This project demonstrates a modern ingestion pipeline using Delta Lake for fast and reliable data analysis.

---

## 📦 Data Source

- **API**: [CoinGecko Public API](https://www.coingecko.com/en/api)
- **Data**: Top cryptocurrencies with market data, price history, and trading volumes.

---

## 🛠️ Tech Stack

- PySpark
- Delta Lake
- Microsoft Fabric (Lakehouse)
- Git & GitHub

---

## 🔁 Pipeline Overview

1. Ingest crypto data from CoinGecko API using PySpark
2. Transform and flatten nested JSON structures
3. Store cleaned data in Delta format
4. Enable querying via Spark SQL on Fabric Lakehouse

---

## 📁 Project Structure

```
delta-lake-crypto-pipeline/
├── notebooks/
│ ├── 01_Ingest_Data.ipynb
│ └── 02_Transform_Store_Delta.ipynb
├── src/
│ └── api_utils.py
├── data/ (optional for local test data)
├── README.md
```

---

## 🏅 Author & Certifications

**Felipe Castro**  
Analytics Engineer @ EPAM Systems  

📜 [PL-300: Power BI Data Analyst](https://learn.microsoft.com/api/credentials/share/en-us/FelipeCastro-8026/F853AABE365874B3?sharingId=13D660F56C1DFFA3)  
📜 [DP-600: Fabric Analytics Engineer](https://learn.microsoft.com/api/credentials/share/en-us/FelipeCastro-8026/6C5A2F5A8A5864FC?sharingId=13D660F56C1DFFA3)  
