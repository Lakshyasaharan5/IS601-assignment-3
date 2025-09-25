import pytest
from calculator.operations import Operations

def test_add():
    # Basic addition
    assert Operations.addition(2, 3) == 5
    # Edge cases
    assert Operations.addition(-1, 1) == 0
    assert Operations.addition(0, 0) == 0
    assert Operations.addition(1.5, 2.5) == 4.0

def test_subtraction():
    # Basic subtraction
    assert Operations.subtraction(5, 3) == 2
    # Edge cases
    assert Operations.subtraction(3, 5) == -2
    assert Operations.subtraction(0, 0) == 0
    assert Operations.subtraction(-5, -5) == 0

def test_multiplication():
    # Basic multiplication
    assert Operations.multiplication(4, 2) == 8
    # Edge cases
    assert Operations.multiplication(-2, 3) == -6
    assert Operations.multiplication(0, 10) == 0
    assert Operations.multiplication(2.5, 4) == 10.0

def test_division():
    # Basic division
    assert Operations.division(10, 2) == 5
    # Negative division
    assert Operations.division(-9, 3) == -3
    # Division by zero
    with pytest.raises(ValueError, match="Can't divide by zero."):
        Operations.division(5, 0)
    # Floating point division
    assert Operations.division(7.5, 2.5) == 3.0
