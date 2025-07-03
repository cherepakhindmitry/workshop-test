import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student  # Импортируем модель

DATABASE_URL = "postgresql://Skypro:12345678@localhost:5432/qa2"

# Создаем подключение
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)


# Создаем таблицы перед тестами
@pytest.fixture(scope="module")
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


# Тест на добавление студента
def test_add_student(setup_database):
    session = Session()
    new_student = Student(name="John Doe", age=20)
    session.add(new_student)
    session.commit()

    # Проверяем, что студент добавлен
    student = session.query(Student).filter_by(name="John Doe").first()
    assert student is not None
    assert student.name == "John Doe"
    assert student.age == 20
    session.close()


# Тест на изменение студента
def test_update_student(setup_database):
    session = Session()
    student = session.query(Student).filter_by(name="John Doe").first()
    student.age = 21
    session.commit()

    # Проверяем, что возраст студента обновился
    updated_student = session.query(Student).filter_by(name="John Doe").first()
    assert updated_student.age == 21
    session.close()


# Тест на удаление студента
def test_delete_student(setup_database):
    session = Session()
    student = session.query(Student).filter_by(name="John Doe").first()
    session.delete(student)
    session.commit()

    # Проверяем, что студент удален
    deleted_student = session.query(Student).filter_by(name="John Doe").first()
    assert deleted_student is None
    session.close()
