# Функция, проверяющая, является ли год високосным
def is_year_leap(year):
    # Год високосный, если он кратен 4, но не кратен 100,
    # либо если он кратен 400 (правило високосного года)
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


# Пример использования функции
year = 2024
result = is_year_leap(year)


# Выводим результат
print(f"Год {year} високосный: {result}")
