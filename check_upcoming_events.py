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
events_to_check = ["Bird City"]

for event in worldstate["data"]:

    start = datetime.fromtimestamp(event["startTime"] / 1000, tz=timezone.utc)
    end = datetime.fromtimestamp(event["endTime"] / 1000, tz=timezone.utc)

    if event["name"] in events_to_check:
        print(event)