articles = [
    {"title": "Python", "is_read": True},
    {"title": "Космос", "is_read": False},
    {"title": "История", "is_read": True},
    {"title": "Наука", "is_read": False},
]

counter = 0
unread_articles = []

for article in articles:
    if article["is_read"] == True:
        continue
    unread_articles.append(article["title"])
    counter += 1
print(unread_articles)
print("Непрочитанных:", counter)
