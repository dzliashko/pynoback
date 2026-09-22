def should_add_to_queue(article):
    return not article["is_read"] and (article["is_starred"] or article["is_saved"])


articles = [
    {"is_read": False, "is_starred": False, "is_saved": False},
    {"is_read": False, "is_starred": False, "is_saved": True},
    {"is_read": False, "is_starred": True, "is_saved": False},
    {"is_read": False, "is_starred": True, "is_saved": True},
    {"is_read": True, "is_starred": False, "is_saved": False},
    {"is_read": True, "is_starred": False, "is_saved": True},
    {"is_read": True, "is_starred": True, "is_saved": False},
    {"is_read": True, "is_starred": True, "is_saved": True},
]

for article in articles:
    print(should_add_to_queue(article))
