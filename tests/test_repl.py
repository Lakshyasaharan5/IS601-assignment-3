import pytest
from calculator.repl import repl
from calculator.operations import Operations

def test_repl_add_and_exit(monkeypatch, capsys):
    inputs = iter(["add 2 3", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    repl()
    captured = capsys.readouterr()
    assert "5.0" in captured.out
    assert "Goodbye!" in captured.out

def test_repl_invalid_command(monkeypatch, capsys):
    inputs = iter(["hello", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    repl()
    captured = capsys.readouterr()
    assert "Unknown command" in captured.out

def test_repl_division_by_zero(monkeypatch, capsys):
    # Test that REPL handles division by zero gracefully
    inputs = iter(["div 5 0", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    repl()
    captured = capsys.readouterr()
    assert "Can't divide by zero." in captured.out

def test_operations_division_by_zero_direct():
    # Also test the direct function for good measure
    with pytest.raises(ValueError, match="Can't divide by zero."):
        Operations.division(5, 0)
