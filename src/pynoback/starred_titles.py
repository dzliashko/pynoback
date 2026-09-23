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


def get_starred_titles(articles):
    starred_articles = []
    for article in articles:
        if article["is_starred"]:
            starred_articles.append(article["title"])
    return starred_articles


print(get_starred_titles(mixed_articles))
print(get_starred_titles([]))
print(get_starred_titles(unstarred_articles))
print(get_starred_titles(single_starred_article))
print(get_starred_titles(mixed_articles))
