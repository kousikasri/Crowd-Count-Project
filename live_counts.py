# This file stores live people counts from YOLO
from collections import defaultdict

live_zone_counts = defaultdict(int)
hourly_history = defaultdict(list)

live_zone_counts = {
    "Zone 1": 0,
    "Zone 2": 0,
    "Zone 3": 0,
    "Zone 4": 0
}

hourly_history = {
    "Zone 1": [],
    "Zone 2": [],
    "Zone 3": [],
    "Zone 4": []
}
