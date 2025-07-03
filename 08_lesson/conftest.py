import pytest
import requests


# Фикстура, возвращающая базовый URL API
@pytest.fixture(scope="session")
def base_url():
    return "https://yougile.com/api-v2"


# Фикстура, возвращающая заголовки с авторизацией
@pytest.fixture(scope="session")
def headers():
    """
    Фикстура для авторизационного заголовка.
    Используется один раз за сессию тестов.
    """
    token = ("YxhAQHgFZs5bQTfiKhsl8h8oU5c-"
             "D0mG8EP0FNzR0wLRQaZZbhA6Z5DpRZCt+Nnn"
             )
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }


# Фикстура, создающая проект перед тестом и возвращающая его данные
@pytest.fixture(scope="function")
def create_project(headers, base_url):
    """
    Фикстура для создания проекта.
    Создаёт проект и возвращает JSON с его данными.
    Используется в тестах, где нужно обновить или получить проект.
    """
    data = {
        "title": "Проект для теста"
    }

    # POST-запрос на создание проекта
    response = requests.post(
        f"{base_url}/projects",
        json=data,
        headers=headers,
        verify=False  # отключаем SSL-проверку (если нужно)
    )

    # Проверка, что проект успешно создан
    assert response.status_code in (200, 201), (
        f"Проект не создан: {response.status_code}, {response.text}"
    )

    # Возвращаем тело ответа (в нем содержится ID и другие поля проекта)
    return response.json()
