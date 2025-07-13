# Импортируем библиотеки для тестов и подключения к базе данных
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student


# Подключение к локальной базе данных PostgreSQL
DATABASE_URL = "postgresql://Skypro:12345678@localhost:5432/qa2"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)


# Фикстура: создание таблицы до всех тестов и удаление после
@pytest.fixture(scope="module")
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


# Фикстура: создаёт сессию SQLAlchemy для каждого теста
@pytest.fixture
def session():
    session = Session()
    yield session
    session.close()


# Фикстура: добавляет студента перед тестом и удаляет его после
@pytest.fixture
def student_fixture(session):
    student = Student(name="Fixture Student", age=25)
    session.add(student)
    session.commit()
    yield student
    session.delete(student)
    session.commit()


# Тест: проверка добавления студента в таблицу
def test_add_student(setup_database, session):
    student = Student(name="Test Student", age=20)
    session.add(student)
    session.commit()
    result = session.query(Student).filter_by(name="Test Student").first()
    assert result is not None
    assert result.age == 20


# Тест: проверка изменения данных студента
def test_update_student(setup_database, student_fixture, session):
    student_fixture.age = 30
    session.commit()
    updated = session.query(Student).filter_by(
        name=student_fixture.name).first()
    assert updated.age == 30


# Тест: проверка удаления студента из таблицы
def test_delete_student(setup_database, student_fixture, session):
    session.delete(student_fixture)
    session.commit()
    deleted = session.query(Student).filter_by(
        name=student_fixture.name).first()
    assert deleted is None
