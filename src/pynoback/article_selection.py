def should_keep(article):
    return article["is_starred"] or article["is_saved"]


articles = [
    {"is_starred": False, "is_saved": False},
    {"is_starred": False, "is_saved": True},
    {"is_starred": True, "is_saved": False},
    {"is_starred": True, "is_saved": True},
]

for article in articles:
    print(should_keep(article))
