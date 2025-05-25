# Класс User хранит информацию о пользователе: имя и фамилия.
class User:
    def __init__(self, first_name, last_name):
        # Сохраняем имя пользователя
        self.first_name = first_name
        # Сохраняем фамилию пользователя
        self.last_name = last_name

    # Метод для вывода имени
    def print_first_name(self):
        print(self.first_name)

    # Метод для вывода фамилии
    def print_last_name(self):
        print(self.last_name)

    # Метод для вывода полного имени (имя + фамилия)
    def print_full_name(self):
        print(f"{self.first_name} {self.last_name}")
