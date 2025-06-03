from string_utils import StringUtils

utils = StringUtils()


def test_capitalize_positive():
    assert utils.capitalize("skypro") == "Skypro"


def test_capitalize_empty_string():
    assert utils.capitalize("") == ""


def test_trim_positive():
    assert utils.trim("   skypro") == "skypro"


def test_trim_no_leading_spaces():
    assert utils.trim("skypro") == "skypro"


def test_contains_positive():
    assert utils.contains("SkyPro", "S") is True


def test_contains_negative():
    assert utils.contains("SkyPro", "X") is False


def test_delete_symbol_positive():
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"


def test_delete_symbol_full_word():
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"


def test_delete_symbol_not_found():
    assert utils.delete_symbol("SkyPro", "Z") == "SkyPro"


def test_delete_symbol_empty_string():
    assert utils.delete_symbol("", "a") == ""
