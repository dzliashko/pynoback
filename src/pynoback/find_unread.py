articles = [
    {"title": "Python", "is_read": True},
    {"title": "Космос", "is_read": False},
    {"title": "Наука", "is_read": False},
]

result = "Непрочитанных нет"

for article in articles:
    if not article["is_read"]:
        result = article["title"]
        break

print(result)
