import pytest
from myfile import check_even_odd

def test_one():
    num = 5
    assert check_even_odd(num) == "Odd"

def test_two():
    num = 5
    assert check_even_odd(num) == "Even"
