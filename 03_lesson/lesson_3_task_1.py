# Импортируем класс User из файла user.py
from user import User

# Создаём объект пользователя с именем и фамилией
my_user = User("Иван", "Иванов")

# Вызываем метод, который печатает имя
my_user.print_first_name()  # Выведет: Иван

# Вызываем метод, который печатает фамилию
my_user.print_last_name()   # Выведет: Иванов

# Вызываем метод, который печатает полное имя
my_user.print_full_name()   # Выведет: Иван Иванов
