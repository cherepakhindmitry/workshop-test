import requests


def test_update_project_positive(base_url, headers, create_project):
    """
    Позитивный тест: обновление названия проекта.
    После PUT-запроса делаем GET-запрос,
    чтобы проверить, что заголовок обновлён.
    """
    project_id = create_project["id"]

    # Шаг 1: обновляем название проекта
    response = requests.put(
        f"{base_url}/projects/{project_id}",
        json={"title": "Обновленное имя"},
        headers=headers
    )

    print("PUT статус:", response.status_code)
    print("PUT ответ:", response.text)
    assert response.status_code == 200

    # Шаг 2: получаем проект заново
    get_response = requests.get(
        f"{base_url}/projects/{project_id}",
        headers=headers
    )

    print("GET статус:", get_response.status_code)
    print("GET ответ:", get_response.text)
    assert get_response.status_code == 200
    assert get_response.json().get("title") == "Обновленное имя"


def test_update_project_negative(base_url, headers):
    response = requests.put(
        f"{base_url}/projects/fake-id",
        json={"title": "Ошибка"},  # ← исправлено
        headers=headers
    )
    print("Статус:", response.status_code)
    print("Ответ:", response.text)
    assert response.status_code == 404
