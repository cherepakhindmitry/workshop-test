# Импорт базовых классов для описания таблицы
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

# Создание базового класса для моделей
Base = declarative_base()


# Описание таблицы студентов
class Student(Base):
    __tablename__ = 'students'

    # Столбцы таблицы
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

    # Представление объекта в виде строки
    def __repr__(self):
        return f"<Student(name={self.name}, age={self.age})>"
