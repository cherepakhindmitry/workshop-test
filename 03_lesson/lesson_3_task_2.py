# Импортируем класс Smartphone из файла smartphone.py
from smartphone import Smartphone

# Создаём список с 5-ю смартфонами
catalog = [
    Smartphone("Apple", "iPhone 13", "+79161234567"),
    Smartphone("Samsung", "Galaxy S21", "+79161234568"),
    Smartphone("Xiaomi", "Redmi Note 10", "+79161234569"),
    Smartphone("Google", "Pixel 6", "+79161234570"),
    Smartphone("OnePlus", "9 Pro", "+79161234571"),
]

# Проходим по каждому телефону и печатаем его данные
for phone in catalog:
    # Формат вывода: Марка - Модель. Номер
    print(f"{phone.brand} - {phone.model}. {phone.number}")
