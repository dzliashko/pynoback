articles = [
    {"title": "Python", "is_read": True},
    {"title": "Космос", "is_read": False},
    {"title": "История", "is_read": True},
    {"title": "Наука", "is_read": False},
]
articles2 = [
    {"title": "Python", "is_read": True},
    {"title": "Космос", "is_read": True},
    {"title": "История", "is_read": True},
    {"title": "Наука", "is_read": True},
]
articles3 = [
    {"title": "Python", "is_read": False},
]


def find_first_unread_title(articles):
    for article in articles:
        if article["is_read"] != True:
            return article["title"]
    return None


print(find_first_unread_title(articles))
print(find_first_unread_title(articles2))
print(find_first_unread_title(articles3))
print(find_first_unread_title([]))
