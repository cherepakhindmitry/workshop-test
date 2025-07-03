# 🔐 Авторизация
# pip install sqlalchemy psycopg2-binary pytest
⚠️ Токен авторизации не включён в репозиторий.

Для запуска тестов необходимо указать валидный токен в conftest.py:
token = "ВАШ_ТОКЕН"

# 🧪 Домашнее задание 8 — API тесты Yougile

Папка `08_lesson` содержит автотесты для API-сервиса [Yougile](https://yougile.com), написанные с использованием `pytest` и `requests`.

---

## 📄 Содержание

| Файл                     | Описание                                                  |
|--------------------------|-----------------------------------------------------------|
| `conftest.py`            | Общие фикстуры: `base_url`, `headers`, `create_project`   |
| `test_create_project.py` | Тесты метода `POST /projects` (создание проекта)          |
| `test_update_project.py` | Тесты метода `PUT /projects/{id}` (обновление проекта)    |
| `test_get_project.py`    | Тесты метода `GET /projects/{id}` (получение проекта)     |

---

## ✅ Проверка flake8

Код проверен линтером `flake8`. Все замечания исправлены:

```bash
python -m flake8 08_lesson

