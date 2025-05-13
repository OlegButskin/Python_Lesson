import pytest
from string_utils import StringUtils


string_utils = StringUtils()

# Тесты для capitalize()
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"), # Латиница
    ("hello world", "Hello world"), # Строка с пробелами
    ("питон", "Питон"), # Кирилица 
    ("", ""), # Верхний регистр
    ("04 april 2023", "04 april 2023"), # Дата с пробелами 
    ("!hello", "!hello"), # Спецсимволы
    ("   sample", "   sample") # Пробелы в начале
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"), # цифры с буквами
    ("", ""), # пустая строка
    ("   ", "   "), # только пробелы
])


def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


 # Тесты для trim()
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),                  # базовый случай
    ("  hello   ", "hello   "),               # пробелы после текста
    ("\t\ttext", "\t\ttext"),                 # табы вместо пробелов
    ("   2023", "2023"),                      # цифры после пробелов
    ("", ""),                                 # пустая строка
    ("   ", ""),                              # только пробелы
    ("no spaces", "no spaces"),               # без пробелов
    (" \t mixed \t ", "\t mixed \t "),        # смешанные пробелы
    (" leading and trailing ", "leading and trailing "),  # пробелы вокруг
    ("   multi   space   ", "multi   space   "),  # множественные пробелы
])
def test_trim(input_str, expected):
    assert string_utils.trim(input_str) == expected   


# Тесты для contains()
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),                    # символ в начале
    ("Python", "thon", True),                 # подстрока
    ("12345", "3", True),                     # цифра
    (" ", " ", True),                         # пробел
    ("SkyPro", "U", False),                   # отсутствующий символ
    ("", "a", False),                         # пустая строка
    ("Multi\nline", "\n", True),              # спецсимвол
    ("Unicode✓", "✓", True),                  # unicode символ
    ("A"*1000, "A", True),                    # большая строка
])
def test_contains(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


    # Тесты для delete_symbol()
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "k", "SyPro"),                 # один символ
    ("abracadabra", "a", "brcdbr"),           # множественные вхождения
    ("Hello World", " ", "HelloWorld"),       # пробел
    ("123-456-789", "-", "123456789"),        # разделитель
    ("Test", "test", "Test"),                 # регистрозависимость
    ("", "a", ""),                            # пустая строка
])

def test_delete_symbol(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected
