import requests

# Тест для получения токена авторизации
def test_get_token(base_url):
    # Отправляем POST-запрос на получение токена
    response = requests.post(f"{base_url}/api-v2/auth/keys/get",  # URL для авторизации
        json={
            # Указываем логин, пароль и ID компании (нужны для входа)
            "login": "cherepakhindmitry@gmail.com",
            "password": "LJYYougile64ru!",
            "companyId": "8770a90e-da00-40e3-990f-9bc29bf93d02"
        },
        verify=False  # отключаем проверку SSL-сертификата (иначе может быть ошибка)
    )

    # Выводим статус ответа и сам токен
    print(response.status_code)
    print(response.text)


def test_get_token(base_url):
    response = requests.post(
        f"{base_url}/auth/keys",  # <== исправленный URL
        json={
            "login": "cherepakhindmitry@gmail.com",
            "password": "LJYYougile64ru!",
            "companyId": "8770a90e-da00-40e3-990f-9bc29bf93d02"
        },
        verify=False  # отключает SSL-проверку
    )

    print(response.status_code)
    print(response.text)

# Тест для получения токена авторизации
def test_token(base_url):
    # Отправляем POST-запрос на получение токена
    response = requests.post(
        f"{base_url}/auth/keys/get",  # URL для авторизации
        json={
            # Указываем логин, пароль и ID компании (нужны для входа)
            "login": "cherepakhindmitry@gmail.com",
            "password": "LJYYougile64ru!",
            "companyId": "8770a90e-da00-40e3-990f-9bc29bf93d02"
        },
        verify=False  # отключаем проверку SSL-сертификата (иначе может быть ошибка)
    )

    # Выводим статус ответа и сам токен
    print(response.status_code)
    print(response.text)