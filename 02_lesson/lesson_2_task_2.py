# Функция, проверяющая, является ли год високосным
def is_year_leap(year):
    return year % 4 == 0

# Пример использования функции
year = 2024
result = is_year_leap(year)

# Выводим результат
print(f"год {year}: {result}")
