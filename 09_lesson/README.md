"""
# Домашнее задание — Урок 9. SQLAlchemy и тесты

## Состав

- `models.py` — модель таблицы `Student`
- `db_connection.py` — подключение к БД PostgreSQL
- `test_operations.py` — три теста: добавление, изменение и удаление записи
- Используется SQLAlchemy и pytest, фикстуры для пред- и постобработки

## Подключение

Строка подключения:
postgresql://Skypro:12345678@localhost:5432/qa2

## Запуск тестов

```bash
python -m pytest 09_lesson/test_operations.py
```

## Инициализация БД вручную

Если таблица отсутствует, запустите:

```bash
python init_db.py
```
"""