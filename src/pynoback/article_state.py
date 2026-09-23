article = {"title": "Космос", "is_read": False, "is_starred": True}


def mark_as_read(article):
    article["is_read"] = True


result = mark_as_read(article)
print(article)
print(result)
mark_as_read(article)
print(article)
