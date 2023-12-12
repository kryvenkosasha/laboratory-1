number = int(input())  

# Перевіряємо, чи число потрапляє у вказаний інтервал
is_in_interval = (-15 < number <= 12) or (14 < number < 17) or (number >= 19)

print(is_in_interval)