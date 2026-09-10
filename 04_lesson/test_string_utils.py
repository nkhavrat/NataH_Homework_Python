import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
 ("python", "Python"),
 ("hello world","Hello world"),
 ("skypro", "Skypro"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected",[
    ("", ""),
    ("  ","  "),
    ("123abc", "123abc"),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected",[
    (" Skypro", "Skypro"),
    (" Skypro ", "Skypro "),
    ("   python", "python"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected",[
    ("345 abc", "345 abc"),
    ("   ",""),
    ("None", "None"),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected",[
    ("Skypro", "p", True),
    ("Skypro", "a", False),
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected",[
    ("Hello", "", True),
    ("", "a", False),
    (None, "a", False),
    ("Hello", None, False),
    ([], [], False),
])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected",[
    ("Skypro", "k", "Sypro"),
    ("Skypro", "pro", "Sky"),
    ("123 abc", " ", "123abc"),
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected",[
    ("", "a", ""),
    ("   ", "a", "   "),
    ("Hello", "a", "Hello"),
    ("Hello", None, "Hello")
])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected
