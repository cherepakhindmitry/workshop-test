# Домашнее задание по уроку 7 — PageObject

## Содержание
- `test_01_calc_po.py` — автотест для калькулятора на сайте bonigarcia.dev
- `test_02_shop_po.py` — автотест для магазина saucedemo.com
- Вся логика вынесена в PageObject-классы (`/pages`)

Страницы PageObject:
Все классы снабжены:

типами аргументов и возвращаемых значений

краткими docstring

4. calc_page.py — калькулятор
5. cart_page.py — корзина
6. checkout_page.py — оформление
7. inventory_page.py — список товаров
8. login_page.py — логин


## Запуск тестов
pytest 10_lessons --alluredir=allure-results

Просмотр отчета

allure serve allure-results
