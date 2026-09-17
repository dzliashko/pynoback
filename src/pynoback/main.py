def count_nonempty_feeds(unread_counts):
    counter = 0
    for i in unread_counts:
        if i > 0:
            counter = counter + 1
    return counter


print(count_nonempty_feeds([3, 0, 5, 2]))
print(count_nonempty_feeds([0, 0]))
print(count_nonempty_feeds([]))
