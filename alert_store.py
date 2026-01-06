alerts_config = {
    "zone1": {"threshold": 20, "enabled": True, "ack": False},
    "zone2": {"threshold": 25, "enabled": True, "ack": False},
    "zone3": {"threshold": 15, "enabled": True, "ack": False},
    "zone4": {"threshold": 10, "enabled": True, "ack": False}
}

alert_logs = []

def update_threshold(zone, threshold, enabled):
    alerts_config[zone]["threshold"] = threshold
    alerts_config[zone]["enabled"] = enabled

def check_alert(zone, count):
    cfg = alerts_config.get(zone)
    if not cfg or not cfg["enabled"]:
        return False

    if count > cfg["threshold"] and zone not in active_alerts:
        raise_alert(zone, count)
        return True
    return False


def acknowledge(zone):
    alerts_config[zone]["ack"] = True

def reset_ack(zone):
    alerts_config[zone]["ack"] = False

def get_config():
    return alerts_config

active_alerts = {}

def raise_alert(zone, count):
    active_alerts[zone] = {
        "zone": zone,
        "count": count
    }

def get_active_alerts():
    return active_alerts

def acknowledge(zone):
    active_alerts.pop(zone, None)
    alerts_config[zone]["ack"] = True
