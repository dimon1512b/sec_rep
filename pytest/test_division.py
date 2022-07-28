from utills.division import division
import pytest


"""
test functions must be started by 'test' keyword
"""


@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 1.0),
    (1, 0, 'Division by zero!'),
])
def test_division_func(a, b, expected):
    assert division(10, 2) == 5.0
