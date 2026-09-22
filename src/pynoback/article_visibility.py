def should_show(article):
    return article["is_starred"] and not article["is_read"]


articles = [
    {"is_starred": False, "is_read": False},
    {"is_starred": False, "is_read": True},
    {"is_starred": True, "is_read": False},
    {"is_starred": True, "is_read": True},
]

for article in articles:
    print(should_show(article))
