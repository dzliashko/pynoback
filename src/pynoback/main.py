def count_nonempty_feeds(unread_counts):
    counter = 0
    for i in unread_counts:
        if i > 0:
            counter = counter + 1
    return counter


print(count_nonempty_feeds([3, 0, 5, 2]))
print(count_nonempty_feeds([0, 0]))
print(count_nonempty_feeds([]))


def get_unread_titles(articles):
    result = []
    for article in articles:
        if article["is_read"] == False:
            result.append(article["title"])
    return result


articles = [
    {"title": "Основы Python", "is_read": False},
    {"title": "Новости науки", "is_read": True},
    {"title": "Космос", "is_read": False},
]

print(get_unread_titles(articles))
