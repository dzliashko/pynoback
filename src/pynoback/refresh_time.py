first_thread_time = float(input("Введите время загрузки 1-ой ленты в секундах: "))
second_thread_time = float(input("Введите время загрузки 2-ой ленты в секундах: "))
total_time = first_thread_time + second_thread_time
average_time = total_time / 2

print(f"Время первой ленты: {first_thread_time}")
print(f"Время второй ленты: {second_thread_time}")
print(f"Общее время: {total_time}")
print(f"Среднее время: {average_time}")
