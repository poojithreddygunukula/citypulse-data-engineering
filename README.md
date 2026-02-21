# 🚦 CityPulse – Urban Data Engineering Pipeline

## 📌 Project Overview

CityPulse is an end-to-end data engineering project that simulates an urban analytics platform.  
It ingests, processes, and analyzes city infrastructure metrics such as traffic congestion, pollution levels, energy usage, and public transport activity.

The goal of this project is to demonstrate:

- Database schema design
- Data ingestion & cleaning
- SQL-based analytics
- Data validation
- Version control best practices
- Production-style project structure

---

## 🏗️ Architecture Overview

Raw Data → Staging Layer → Analytics Layer → SQL Insights

### Layers:

1. **Raw Layer**
   - Simulated city metrics dataset
   - CSV ingestion into PostgreSQL

2. **Staging Layer**
   - Data cleaning
   - Null handling
   - Type corrections
   - Quality checks

3. **Analytics Layer**
   - Aggregations
   - KPI calculations
   - Metric validation queries

---

## 🛠️ Tech Stack

- PostgreSQL
- SQL
- Git & GitHub
- macOS Terminal
- SSH Authentication

---

## 📂 Database Schema

Schema: `analytics`

Main Table:
`analytics.city_metrics`

### Key Columns:
- city_id
- metric_name
- metric_value
- recorded_at

---

## 📊 Example Analytics Query

Count total vs non-null congestion records:

```sql
SELECT
    COUNT(*) AS total,
    COUNT(metric_value) AS non_null
FROM analytics.city_metrics
WHERE metric_name = 'congestion_level';
```

This validates data completeness and ingestion accuracy.

## 🔎 Data Validation Checks Performed

-> Row count validation
-> Null percentage checks
-> Metric-specific filtering
-> Aggregation verification
-> Schema consistency checks

## 🚀 How to Run This Project
## 1️⃣ Clone Repository

git clone git@github.com:poojithreddygunukula/citypulse-data-engineering.git
cd citypulse-data-engineering

## 2️⃣ Start PostgreSQL
Ensure PostgreSQL is running.

## 3️⃣ Connect to Database
psql -d citypulse

## 4️⃣ Run SQL Scripts
Execute schema creation and data load scripts inside psql.

## 🧠 What This Project Demonstrates

✔ Data modeling
✔ SQL analytics
✔ Production-style project structure
✔ Git version control
✔ SSH-based GitHub authentication
✔ End-to-end data validation

## 📈 Future Improvements

- Deploy PostgreSQL to Google Cloud SQL
- Store raw data in Google Cloud Storage
- Build analytics layer using BigQuery
- Orchestrate workflows using Cloud Composer (Apache Airflow)
- Containerize pipeline using Docker
- Deploy transformations using dbt
- Implement CI/CD with GitHub Actions
- Add data quality checks with Great Expectations
- Create monitoring & logging using Cloud Monitoring
- Build a dashboard layer using Looker Studio
- Implement incremental data loading strategy
- Add partitioning & clustering for BigQuery optimization

## 👨‍💻 Author

Poojith Reddy Gunukula
Data Engineering Enthusiast

GitHub: https://github.com/poojithreddygunukula
