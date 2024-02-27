import pytest

from src.lesson_12_2_3 import divide


def test_divide():
    assert divide(50, 2) == 25
    assert divide(50, 10) == 5
    assert divide(50, 5) == 10
    assert divide(6.6, 2) == 3.3
    assert divide(100, 100) == 1


def test_divide_division_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)