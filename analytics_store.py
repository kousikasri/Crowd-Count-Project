import time

history = []

zone_counts = {
    "zone1": [],
    "zone2": [],
    "zone3": [],
    "zone4": []
}

def update_zone_count(zone, count):
    zone_counts[zone].append(count)

    # limit memory
    if len(zone_counts[zone]) > 50:
        zone_counts[zone].pop(0)

def get_zone_counts(zone):
    return zone_counts.get(zone, [])


def store_history(camera_id, zone_id, count):
    history.append({
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "camera_id": camera_id,
        "zone_id": zone_id,
        "count": count
    })

def get_history():
    return history
