from string_calculator import add
import pytest

def test_empty_string_returns_zero():
    assert add("") == 0

def test_single_number_returns_value():
    assert add("1") == 1

def test_two_numbers_comma_separated():
    assert add("1,5") == 6

def test_newline_between_numbers():
    assert add("1\n2,3") == 6

def test_custom_single_char_delimiter():
    assert add("//;\n1;2") == 3