import math

# Функция для вычисления площади квадрата
def square(side):
    # Вычисляем площадь и округляем вверх, если дробное
    return math.ceil(side ** 2)

# Пример вызова
print(square(4.2))  # Вывод: 18
