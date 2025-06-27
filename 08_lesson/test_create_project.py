import requests


# Позитивный тест: создание проекта с валидными данными
def test_create_project(base_url, headers):
    url = f"{base_url}/projects"  # URL для создания проекта

    data = {
        "title": "Проект для теста"  # тело запроса — название нового проекта
    }

    # Отправляем POST-запрос на создание проекта
    response = requests.post(url, json=data, headers=headers, verify=False)

    # Выводим статус ответа и текст (тело ответа
    # должно содержать ID нового проекта)
    print("Статус:", response.status_code)
    print("Ответ:", response.text)


# Негативный тест: создание проекта с пустым заголовком
def test_create_project_negative(base_url, headers):
    # Негативный тест: попытка создать проект с пустым названием.
    # Ожидается ошибка 400 или 422.
    url = f"{base_url}/projects"

    data = {
        "title": ""  # передаём пустой заголовок
    }

    # Отправляем POST-запрос
    response = requests.post(url, json=data, headers=headers, verify=False)

    # Проверяем, что сервер вернёт ошибку (ожидается 400 или 422)
    assert response.status_code in (400, 422), (
        f"Ожидался 400 или 422, получен {response.status_code}"
    )
