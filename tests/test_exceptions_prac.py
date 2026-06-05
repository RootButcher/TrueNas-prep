import pytest
from practice.exceptions_prac import *


@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5.0),
    (5, 0, float('inf')),
    (0, 5, 0.0),
    (-10, 2, -5.0),
    (10, -2, -5.0),
    (-10, -2, 5.0),
    (0, 0, float('inf')),
])
def test_safe_divide(a, b, expected):
    assert safe_divide(a, b) == expected

@pytest.mark.parametrize("a, b, expected, exception", [
    (10, 2, 5.0, False),
    (0, 5, 0.0, False),
    (0, 5 ,0, False),
    (0, 0, 0.0, True),
    (5, 0, 0.0, True),
])
def test_divide(a, b, expected, exception):
    if exception:
        with pytest.raises(ZeroDivisionError):
            divide(a, b)
    else:
        assert divide(a, b) == expected


@pytest.mark.parametrize("size, expected", [
    ("1K", 1024),
    ("2M", 2 * 1024 ** 2),
    ("3G", 3 * 1024 ** 3),
    ("512", 512),
    ("0", 0),
    ("1K ", 1024),
    ("1K\n", 1024),
    ("1K\t", 1024),
    (" 1K\t", 1024),
])
def test_parse_size(size, expected):
    assert parse_size(size) == expected

@pytest.mark.parametrize("size", ["1k", "2m", "3g", "512.5", "-10", ".5", "10X"])
def test_parse_size_value_error(size):
    with pytest.raises(ValueError):
        parse_size(size)
