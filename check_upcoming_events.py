import requests
from datetime import datetime, timezone

url = "https://metaforge.app/api/arc-raiders/events-schedule"
response = requests.get(url)
worldstate = response.json()

# INIT
now = datetime.now(timezone.utc)
upcoming_events = []

"""
Major:
Close Scrutiny, Cold Snap, Night Raid, ~

Minor:
Harvester, Matriach, Husk Graveyard, Bird City, ~
"""
events_to_check = ["Locked Gate"]

def convertTime(event,time):
    return datetime.fromtimestamp(event[time] / 1000, tz=timezone.utc)

for event in worldstate["data"]:

    if event["name"] in events_to_check:

        start = convertTime(event,"startTime")
        end = convertTime(event,"endTime")

        if start > now:
            upcoming_events.append({
                "name": event["name"],
                "map": event["map"],
                "startTime": start,
                "endTime": end
            })


# filtered_events.sort(key=lambda x: x["start"])
# filtered_events.sort(key=lambda x: (x["event"]["name"], x["start"]))
print(f"Now: {now}")
for eventReal in upcoming_events[:3]:
    print(f"Condition: {eventReal["name"]}")
    print(f"Map: {eventReal["map"]}")
    print(f"Start Time: {eventReal["startTime"]}")
    print(f"End Time: {eventReal["endTime"]}")