article = {"title": "Космос", "is_read": False, "is_starred": True}


def mark_as_read(article):
    article["is_read"] = True


# result = mark_as_read(article)
# print(article)
# print(result)
# mark_as_read(article)
# print(article)


articles = [
    {"title": "Python", "is_read": False},
    {"title": "Космос", "is_read": True},
    {"title": "Наука", "is_read": False},
]


def mark_all_as_read(articles):
    counter = 0
    for article in articles:
        if not article["is_read"]:
            counter += 1
        mark_as_read(article)
    return counter


print(mark_all_as_read(articles))
print(articles)
print(mark_all_as_read(articles))
print(mark_all_as_read([]))
