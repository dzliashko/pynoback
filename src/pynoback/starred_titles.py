mixed_articles = [
    {"title": "Python", "is_starred": True},
    {"title": "Космос", "is_starred": False},
    {"title": "Наука", "is_starred": True},
]

unstarred_articles = [
    {"title": "История", "is_starred": False},
]

single_starred_article = [
    {"title": "Музыка", "is_starred": True},
]


def describe_starred(articles):
    starred = get_starred_titles(articles)
    count = len(starred)
    if count == 0:
        return "Избранных статей нет"
    return f"Избранных статей: {count}"


def get_starred_titles(articles):
    starred_titles = []
    for article in articles:
        if article["is_starred"]:
            starred_titles.append(article["title"])
    return starred_titles


print(get_starred_titles(mixed_articles))
print(get_starred_titles([]))
print(get_starred_titles(unstarred_articles))
print(get_starred_titles(single_starred_article))
print(get_starred_titles(mixed_articles))

print(describe_starred(mixed_articles))
print(describe_starred([]))
print(describe_starred(single_starred_article))
