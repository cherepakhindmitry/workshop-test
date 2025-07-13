# Импортируем базовую модель и движок подключения к базе
from models import Base
from db_connection import engine

# Создание всех таблиц, описанных через Base (в данном случае — students)
Base.metadata.create_all(bind=engine)

# Выводим сообщение об успешном создании
print("Таблица students создана.")
