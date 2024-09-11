import pytest
from HW_1.myfile import check_even_odd

def test_one():
    num = 5
    assert check_even_odd(num) == "Odd"

def test_two():
    num = 9
    assert check_even_odd(num) == "Even"
