import random
import uuid
from datetime import datetime, timedelta
import csv

CITY_ZONES = [
    "Downtown",
    "Uptown",
    "Midtown",
    "Industrial",
    "Residential"
]

EVENT_TYPES = [
    "traffic",
    "air_quality",
    "power",
    "emergency"
]

def random_timestamp(days_back=7):
    now = datetime.now()
    delta = timedelta(
        days=random.randint(0, days_back),
        hours=random.randint(0, 23),
        minutes=random.randint(0, 59)
    )
    return now - delta

def generate_event():
    event_type = random.choice(EVENT_TYPES)

    event = {
        "event_id": str(uuid.uuid4()),
        "event_type": event_type,
        "event_time": random_timestamp().isoformat(),
        "city_zone": random.choice(CITY_ZONES),
        "source": f"{event_type}_sensor"
    }

    if event_type == "traffic":
        event.update({
            "vehicle_count": random.randint(20, 500),
            "congestion_level": random.choice(["low", "medium", "high"])
        })

    elif event_type == "air_quality":
        event.update({
            "aqi": random.randint(50, 200),
            "pm25": round(random.uniform(10, 80), 2),
            "pm10": round(random.uniform(20, 150), 2)
        })

    elif event_type == "power":
        event.update({
            "consumption_kwh": round(random.uniform(5, 100), 2)
        })

    elif event_type == "emergency":
        event.update({
            "incident_type": random.choice(["fire", "medical", "accident"])
        })

    return event

def write_events_to_csv(filename, num_events=500):
    events = [generate_event() for _ in range(num_events)]

    fieldnames = set()
    for event in events:
        fieldnames.update(event.keys())

    fieldnames = sorted(fieldnames)

    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(events)

    print(f"Generated {num_events} events → {filename}")

if __name__ == "__main__":
    write_events_to_csv("city_events.csv", num_events=1000)
