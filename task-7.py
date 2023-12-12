# Отримуємо три цілі числа
a = int(input())
b = int(input())
c = int(input())

# Знаходимо максимальне, мінімальне та залишкове число
maximum = max(a, b, c)
minimum = min(a, b, c)
middle = (a + b + c) - maximum - minimum

# Виводимо результат у трьох рядках
print(maximum)
print(minimum)
print(middle)
