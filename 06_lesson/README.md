# Домашнее задание 6 — Selenium: ожидания

## Что делал:

* Создал новую ветку `lesson6`
* Создал папку `06_lesson`
* Написал 3 скрипта:

  * `lesson06_task1.py` — нажатие кнопки с ожиданием
  * `lesson06_task2.py` — ввод текста и смена кнопки
  * `lesson06_task3.py` — загрузка картинок
* Использовал **WebDriverWait** и **expected\_conditions**
* **Не использовал `sleep()`** — как по условиям
* Установил flake8 и проверил стиль кода

## Команды:

### Структура и файлы:

```bash
cd workshop-test
mkdir 06_lesson
cd 06_lesson
New-Item lesson06_task1.py -ItemType File
New-Item lesson06_task2.py -ItemType File
New-Item lesson06_task3.py -ItemType File
New-Item README.md -ItemType File
```

### Установка flake8:

```bash
python -m pip install flake8
```

### Проверка стиля:

```bash
cd workshop-test
python -m flake8 06_lesson
```

### Git:

```bash
git checkout -b lesson6
git add 06_lesson
git commit -m "Домашка 6: ожидания в Selenium"
git push origin lesson6
```

### Pull Request:

* Перейти на GitHub
* Создать PR из `lesson6` в `main`
* Добавить описание и отправить на проверку

## Заметки:

* Во всех заданиях обязательно использовать `WebDriverWait`, `EC`
* Проверить, что текст / src появляется — не сразу
* Для изображений задание использует атрибут `src` у 3-й картинки
