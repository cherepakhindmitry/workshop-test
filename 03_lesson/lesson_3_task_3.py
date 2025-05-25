# Импортируем нужные классы
from address import Address
from mailing import Mailing

# Создаём адрес получателя
to_addr = Address("101000", "Москва", "Тверская", "1", "10")

# Создаём адрес отправителя
from_addr = Address("190000", "Санкт-Петербург", "Невский", "5", "25")

# Создаём объект отправления, передаём адреса, стоимость и трек-номер
mail = Mailing(to_addr, from_addr, 350, "AB123456789RU")

# Печатаем информацию об отправлении
print(
    f"Отправление {mail.track} из {mail.from_address.index}, "
    f"{mail.from_address.city}, "
    f"{mail.from_address.street}, "
    f"{mail.from_address.house} - {mail.from_address.apartment} в "
    f"{mail.to_address.index}, "
    f"{mail.to_address.city}, "
    f"{mail.to_address.street}, "
    f"{mail.to_address.house} - {mail.to_address.apartment}. "
    f"Стоимость {mail.cost} рублей."
)

# Пример вывода:
# Отправление AB123456789RU из 190000, Санкт-Петербург, Невский, 5 - 25 в
# 101000, Москва, Тверская, 1 - 10. Стоимость 350 рублей.
