# Класс Address описывает почтовый адрес:
# индекс, город, улица, дом и квартира
class Address:
    def __init__(self, index, city, street, house, apartment):
        self.index = index        # Почтовый индекс (например, 101000)
        self.city = city          # Город (например, Москва)
        self.street = street      # Улица (например, Тверская)
        self.house = house        # Номер дома (например, 1)
        self.apartment = apartment  # Номер квартиры (например, 10)
