Урок 9. Работа с базой данных через SQLAlchemy
В этом задании реализованы тесты взаимодействия с базой данных PostgreSQL с использованием SQLAlchemy.

Структура:
models.py — описание модели Student.

db_connection.py — подключение к базе данных.

init_db.py — создание таблиц.

test_operations.py — автотесты на добавление, изменение и удаление студентов.

Возможности:
Подключение к PostgreSQL через SQLAlchemy

Создание таблицы students

CRUD-операции через ORM

Автотесты с использованием pytest и фикстур

Прогон тестов:
python -m pytest 09_lesson/test_operations.py

✅ Проверка синтаксиса:
flake8 09_lesson