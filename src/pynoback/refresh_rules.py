def should_refresh(feed):
    return feed["is_enabled"] and feed["minutes_since_refresh"] >= 30


feeds = [
    {"is_enabled": True, "minutes_since_refresh": 45},
    {"is_enabled": True, "minutes_since_refresh": 29},
    {"is_enabled": False, "minutes_since_refresh": 45},
    {"is_enabled": True, "minutes_since_refresh": 30},
]

for feed in feeds:
    print(should_refresh(feed))
