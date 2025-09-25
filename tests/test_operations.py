import pytest
from calculator.operations import Operations

# ---------- ADDITION TESTS ----------

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (-5, -5, -10),
    (-5, 10, 5),
    (0, 5, 5),
    (1_000_000, 2_000_000, 3_000_000),
    (2.5, 3.5, 6.0),
    (0.1, 0.2, 0.3),
    (-2.5, 5.0, 2.5),
])
def test_addition_cases(a, b, expected):
    assert round(Operations.addition(a, b), 6) == round(expected, 6)

# ---------- SUBTRACTION TESTS ----------

@pytest.mark.parametrize("a,b,expected", [
    (5, 3, 2),
    (-5, -3, -2),
    (0, 5, -5),
    (5, 5, 0),
    (1_000_000, 500_000, 500_000),
    (5.5, 2.2, 3.3),
    (2, 10, -8),
])
def test_subtraction_cases(a, b, expected):
    assert round(Operations.subtraction(a, b), 6) == round(expected, 6)

# ---------- MULTIPLICATION TESTS ----------

@pytest.mark.parametrize("a,b,expected", [
    (4, 2, 8),
    (-4, 2, -8),
    (-4, -2, 8),
    (0, 100, 0),
    (1_000, 1_000, 1_000_000),
    (2.5, 4.0, 10.0),
    (0.5, 0.2, 0.1),
    (-2.5, 4.0, -10.0),
])
def test_multiplication_cases(a, b, expected):
    assert round(Operations.multiplication(a, b), 6) == round(expected, 6)

# ---------- DIVISION TESTS ----------

@pytest.mark.parametrize("a,b,expected", [
    (10, 2, 5),
    (-10, 2, -5),
    (10, -2, -5),
    (-10, -2, 5),
    (7.5, 2.5, 3.0),
    (1, 2, 0.5),
    (1_000_000, 1_000, 1000),
    (0, 5, 0),
])
def test_division_cases(a, b, expected):
    assert round(Operations.division(a, b), 6) == round(expected, 6)

def test_division_by_zero():
    with pytest.raises(ValueError, match="Can't divide by zero."):
        Operations.division(5, 0)
