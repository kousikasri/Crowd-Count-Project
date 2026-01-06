zones = []

def add_zone(zone):
    zones.append(zone)

def get_zones():
    return zones

def update_zone(updated):
    for z in zones:
        if z["id"] == updated["id"]:
            z.update(updated)

def delete_zone(zone_id):
    global zones
    zones = [z for z in zones if z["id"] != zone_id]
