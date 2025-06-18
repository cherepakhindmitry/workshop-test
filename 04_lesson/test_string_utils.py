from string_utils import StringUtils

utils = StringUtils()

# Проверяет, что capitalize делает первую букву заглавной
def test_capitalize_positive():
    assert utils.capitalize("skypro") == "Skypro"

# Проверяет, что capitalize корректно обрабатывает пустую строку
def test_capitalize_empty_string():
    assert utils.capitalize("") == ""


# Проверяет, что trim удаляет пробелы в начале строки
def test_trim_positive():
    assert utils.trim("   skypro") == "skypro"


# Проверяет, что trim не изменяет строку без пробелов в начале
def test_trim_no_leading_spaces():
    assert utils.trim("skypro") == "skypro"


# Проверяет, что contains возвращает True, если символ найден
def test_contains_positive():
    assert utils.contains("SkyPro", "S") == True


# Проверяет, что contains возвращает False, если символ не найден
def test_contains_negative():
    assert utils.contains("SkyPro", "X") is False


# Проверяет, что delete_symbol удаляет символ из строки
def test_delete_symbol_positive():
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"


# Проверяет, что delete_symbol удаляет подстроку целиком
def test_delete_symbol_full_word():
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"


# Проверяет, что delete_symbol не меняет строку, если символ не найден
def test_delete_symbol_not_found():
    assert utils.delete_symbol("SkyPro", "Z") == "SkyPro"


# Проверяет, что delete_symbol корректно работает с пустой строкой
def test_delete_symbol_empty_string():
    assert utils.delete_symbol("", "a") == ""
