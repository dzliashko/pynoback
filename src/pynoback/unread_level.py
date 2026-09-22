def describe_unread_level(count):
    if count == 0:
        return "Всё прочитано"
    elif count <= 10:
        return "Немного статей"
    elif count <= 50:
        return "Много статей"
    else:
        return "Пора разгребать"


counters = (0, 1, 10, 11, 50, 51)

for counter in counters:
    print(describe_unread_level(counter))
