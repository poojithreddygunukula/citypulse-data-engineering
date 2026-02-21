import pandas as pd
import psycopg2

DB_CONFIG = {
    "dbname": "citypulse",
    "user": "saipoojithreddygunukula",
    "password": "None",
    "host": "localhost",
    "port": 5432
}

CITY_NAME = "Birmingham"

METRIC_COLUMNS = [
    "aqi",
    "pm25",
    "pm10",
    "vehicle_count",
    "congestion_level",
    "consumption_kwh"
]

def ingest():
    df = pd.read_csv("data/city_events.csv")

    print("CSV Columns:", df.columns)

    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    for _, row in df.iterrows():
        for metric in METRIC_COLUMNS:
            if metric in df.columns and pd.notna(row[metric]):
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
 VALUES (%s, %s, %s, %s)
                    """,
                    (
                        CITY_NAME,
                        metric,
                        row["event_time"],
                        float(row[metric])
                    )
                )

    conn.commit()
    cur.close()
    conn.close()

    print("Ingestion completed successfully.")

if __name__ == "__main__":
    ingest()

