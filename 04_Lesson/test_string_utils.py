import pytest
from string_utils import StringUtils

string_utils = StringUtils()

# Тесты для capitalize()
@pytest.mark.positive
@pytest.mark.parametrize
("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("04 april 2023", "04 april 2023"),  # строка с числами
    ("two\nlines", "Two\nlines"),        # строка с переносом
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
    ("Already Capitalized", "Already Capitalized"),
    ("!@#$%", "!@#$%"),  # специальные символы
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

# Тесты для trim()
@pytest.mark.positive
@pytest.mark.parametrize
("input_str, expected", [
    ("   skypro", "skypro"),
    ("  hello   ", "hello   "),
    ("\t\ttext", "\t\ttext"),  # табы не удаляются
    ("   2023", "2023"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize
("input_str, expected", [
    ("", ""),
    ("test", "test"),
    ("   ", ""),  # только пробелы
    ("no spaces here", "no spaces here"),
    (None, None),  # проверка на None
])
def test_trim_negative
(input_str, expected):
    if input_str is None:
        with pytest.raises(AttributeError):
            string_utils.trim(input_str)
    else:
        assert string_utils.trim(input_str) == expected

# Тесты для contains()
@pytest.mark.positive
@pytest.mark.parametrize
("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("Python", "thon", True),
    ("12345", "3", True),
    (" ", " ", True),
])
def test_contains_positive
(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize
("string, symbol, expected", [
    ("SkyPro", "U", False),
    ("", "a", False),
    ("Hello", "", False),
    ("Text", "t", False),  # регистрозависимость
    (None, "a", False),
])
def test_contains_negative
(string, symbol, expected):
    if string is None or symbol is None:
        with pytest.raises(TypeError):
            string_utils.contains(string, symbol)
    else:
        assert string_utils.contains(string, symbol) == expected

# Тесты для delete_symbol()
@pytest.mark.positive
@pytest.mark.parametrize
("input_str, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("abracadabra", "a", "brcdbr"),
    ("Hello World", " ", "HelloWorld"),
    ("123-456-789", "-", "123456789"),
])
def test_delete_symbol_positive
(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize
("input_str, symbol, expected", [
    ("Test", "test", "Test"),  # регистрозависимость
    ("", "a", ""),
    ("Hello", "", "Hello"),
    (None, "a", None),
    ("No changes", "z", "No changes"),
])
def test_delete_symbol_negative(input_str, symbol, expected):
    if input_str is None or symbol is None:
        with pytest.raises(TypeError):
            string_utils.delete_symbol(input_str, symbol)
    else:
        assert string_utils.delete_symbol(input_str, symbol) == expected
