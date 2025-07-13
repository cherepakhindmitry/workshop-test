# Импорт базового класса и движка
from models import Base
from db_connection import engine

# Создание всех таблиц, описанных в моделях
Base.metadata.create_all(bind=engine)

# Вывод сообщения для подтверждения
print("Таблица students создана.")
