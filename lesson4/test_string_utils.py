import pytest
from string_utils import StringUtils


string_utils = StringUtils()


# Тестируем метод input_str
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("Тест", "Тест"),
    ("123", "123"),
    ("04 апреля 2023", "04 апреля 2023")
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    (" ", " ")
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


def test_capitalize_negative_with_none():
    with pytest.raises(AttributeError) as excinfo:
        string_utils.capitalize(None)
    assert str(excinfo.value) == ("'NoneType' object has"
                                  " no attribute 'capitalize'")


def test_capitalize_negative_with_empty_list():
    with pytest.raises(AttributeError) as excinfo:
        string_utils.capitalize([])
    assert str(excinfo.value) == "'list' object has no attribute 'capitalize'"


# Тестируем метод trim
@pytest.mark.positive
@pytest.mark.parametrize("trim, expected", [
    (" skypro", "skypro"),
    (" hello world", "hello world"),
    (" тест", "тест"),
    (" 123", "123"),
    (" 04 апреля 2023", "04 апреля 2023")
])
def test_trim_positive(trim, expected):
    assert string_utils.trim(trim) == expected


@pytest.mark.negative
@pytest.mark.parametrize("trim, expected", [
    ("1 23abc", "1 23abc"),
    ("", ""),
    (" ", "")
])
def test_trim_negative(trim, expected):
    assert string_utils.trim(trim) == expected


# Тестируем метод contains
@pytest.mark.positive
@pytest.mark.parametrize("input_string, symbol, expected", [
    ("Skypro", "a", False),
    ("Skyeng", "k", True),
    ("Skyeng", "h", False),

])
def test_contains_positive(input_string, symbol, expected):
    assert string_utils.contains(input_string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_string, symbol, expected", [
    ("skypro", "L", False),
    ("skypro", "!", False),
    ("skypro", "$", False)
])
def test_contains_negative(input_string, symbol, expected):
    assert string_utils.contains(input_string, symbol) == expected


# Тестируем метод delete
@pytest.mark.positive
@pytest.mark.parametrize("input_string, symbol, expected", [
    ("skypro", "pr", "skyo"),
    ("skypro", "pro", "sky"),
    ("skypro", "sky", "pro"),
    ("skypro", "sk", "ypro"),

])
def test_delete_symbol_positive(input_string, symbol, expected):
    assert string_utils.delete_symbol(input_string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_string, symbol, expected", [
    ("Skypro", "L", "Skypro"),
    ("Skypro", "!", "Skypro"),
    ("Skypro", "$", "Skypro")
])
def test_delete_symbol_negative(input_string, symbol, expected):
    assert string_utils.delete_symbol(input_string, symbol) == expected
