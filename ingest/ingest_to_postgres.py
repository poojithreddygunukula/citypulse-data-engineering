import pandas as pd
import psycopg2
from pathlib import Path

# --------------------------------------------------
# Database configuration (macOS + Homebrew Postgres)
# --------------------------------------------------
DB_CONFIG = {
    "dbname": "citypulse",
    "user": "saipoojithreddygunukula",
    "host": "localhost",
    "port": 5432
}

# --------------------------------------------------
# Resolve CSV path safely (no relative path bugs)
# --------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
CSV_PATH = BASE_DIR / "data" / "city_events.csv"

# --------------------------------------------------
# Ingestion logic
# --------------------------------------------------
def ingest():
    # Load CSV
    df = pd.read_csv(CSV_PATH)
    print("CSV Columns:", df.columns)

    # Connect to Postgres
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    # Insert rows safely
    for _, row in df.iterrows():
        cur.execute(
            """
            INSERT INTO city_events_raw (
                event_time,
                event_type,
                city_zone,
                aqi,
                pm25,
                pm10,
                vehicle_count,
                congestion_level,
                consumption_kwh,
                incident_type,
                source
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                row["event_time"],
                row["event_type"],
                row["city_zone"],
                float(row["aqi"]) if pd.notna(row["aqi"]) else None,
                float(row["pm25"]) if pd.notna(row["pm25"]) else None,
                float(row["pm10"]) if pd.notna(row["pm10"]) else None,
                float(row["vehicle_count"]) if pd.notna(row["vehicle_count"]) else None,
                row["congestion_level"],
                float(row["consumption_kwh"]) if pd.notna(row["consumption_kwh"]) else None,
                row["incident_type"],
                row["source"]
            )
        )

    conn.commit()
    cur.close()
    conn.close()

    print("✅ Ingestion completed successfully.")

# --------------------------------------------------
# Entry point
# --------------------------------------------------
if __name__ == "__main__":
    ingest()

