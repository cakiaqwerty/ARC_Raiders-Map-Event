import requests
from datetime import datetime, timezone

url = "https://metaforge.app/api/arc-raiders/events-schedule"
response = requests.get(url)
worldstate = response.json()

# INIT
now = datetime.now(timezone.utc)
active_events = []

# Dictionary
#name = condition
#map
#startTime
#endTime

# print(worldstate["data"][0])

for event in worldstate["data"]:
    # print("Event:", event["name"])
    # print("Map:", event["map"])
    # print("startTimes:", event.get("startTime"))
    # print("endTimes:", event.get("endTime"))
    # print("-" * 40)
    start = datetime.fromtimestamp(event["startTime"] / 1000, tz=timezone.utc)
    end = datetime.fromtimestamp(event["endTime"] / 1000, tz=timezone.utc)

    if start <= now <= end:
        active_events.append({
            "name": event["name"],
            "map": event["map"],
            "start": start,
            "end": end
        })

# Output
for e in active_events:
    print(e["name"], "-", e["map"])
    print("Start (UTC):", e["start"])
    print("End   (UTC):", e["end"])
    print("-" * 30)