import requests


# Базовый URL API Yougile
def test_get_project_positive(base_url, headers, create_project):
    """
    Позитивный тест: получение информации о проекте по его ID.

    1. Сначала используется фикстура create_project, которая создаёт проект
       и возвращает его данные (включая ID).
    2. Затем по этому ID отправляется GET-запрос.
    3. Ожидаем, что статус ответа будет 200 (успешно),
       и в теле ответа должен быть тот же ID, что и у созданного проекта.
    """

    # Получаем ID только что созданного проекта
    project_id = create_project["id"]

    # Отправляем GET-запрос на получение проекта по ID
    response = requests.get(
        f"{base_url}/projects/{project_id}", headers=headers
    )

    # Проверяем, что сервер вернул статус 200 (успешно)
    assert response.status_code == 200

    # Проверяем, что в ответе содержится нужный ID проекта
    assert response.json()["id"] == project_id


def test_get_project_negative(base_url, headers):
    """
    Негативный тест: попытка получить несуществующий проект по фальшивому ID.

    1. Отправляется GET-запрос на проект с ID "fake-id".
    2. Такого проекта нет, поэтому ожидаем статус 404 (Not Found).
    """

    # Отправляем GET-запрос на фейковый (несуществующий) ID проекта
    response = requests.get(f"{base_url}/projects/fake-id", headers=headers)

    # Проверяем, что сервер вернул статус 404 (не найдено)
    assert response.status_code == 404
