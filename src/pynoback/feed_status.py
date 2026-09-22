def describe_unread(feed):
    if feed["unread_count"] is None:
        return "Количество неизвестно"
    if feed["unread_count"] == 0:
        return "Непрочитанных нет"
    return f"Непрочитанных: {feed['unread_count']}"


print(describe_unread({"unread_count": None}))
print(describe_unread({"unread_count": 0}))
print(describe_unread({"unread_count": 5}))
