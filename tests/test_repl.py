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

def test_repl_add_command(monkeypatch, capsys):
    """Test a simple add command in the REPL."""
    inputs = iter(["add 10 5", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    repl()
    out = capsys.readouterr().out
    assert "15.0" in out
    assert "Goodbye!" in out

def test_repl_sub_command(monkeypatch, capsys):
    """Test a simple subtraction command in the REPL."""
    inputs = iter(["sub 10 5", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    repl()
    out = capsys.readouterr().out
    assert "5.0" in out  # 10 - 5 = 5
    assert "Goodbye!" in out

def test_repl_mul_command(monkeypatch, capsys):
    """Test a simple multiplication command in the REPL."""
    inputs = iter(["mul 4 5", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    repl()
    out = capsys.readouterr().out
    assert "20.0" in out  # 4 * 5 = 20
    assert "Goodbye!" in out


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

def test_repl_empty_input(monkeypatch, capsys):
    inputs = iter(["", "exit"])  # simulate pressing Enter
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    repl()
    captured = capsys.readouterr()
    assert "Goodbye!" in captured.out  # just check REPL exits normally

def test_repl_usage_message(monkeypatch, capsys):
    inputs = iter(["add 5", "exit"])  # only one number instead of two
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    repl()
    captured = capsys.readouterr()
    assert "Usage:" in captured.out

def test_repl_value_error_message(monkeypatch, capsys):
    inputs = iter(["add x y", "exit"])  # non-numeric input
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    repl()
    captured = capsys.readouterr()
    assert "Error: Please provide two numbers" in captured.out

def test_repl_division_by_zero_and_continue(monkeypatch, capsys):
    # Try division by zero, then a valid add command to ensure 'continue' is executed
    inputs = iter(["div 5 0", "add 1 1", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    repl()
    captured = capsys.readouterr()

    # Confirm division by zero message is printed
    assert "Can't divide by zero." in captured.out
    # Confirm the loop continued and 'add' worked
    assert "2.0" in captured.out

def test_repl_division_by_zero_only(monkeypatch, capsys):
    # Only division by zero, then exit
    inputs = iter(["div 5 0", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    repl()
    out = capsys.readouterr().out
    # Confirm the printed exception message
    assert "Can't divide by zero." in out

def test_repl_division_then_add(monkeypatch, capsys):
    # Trigger division error, REPL continues, then add
    inputs = iter(["div 1 0", "add 10 20", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    repl()
    out = capsys.readouterr().out
    assert "Can't divide by zero." in out
    assert "30.0" in out  # proves REPL continued after exception

def test_repl_all_branches(monkeypatch, capsys):
    inputs = iter([
        "",                     # empty input
        "add 5",                # wrong arg count
        "add x y",              # ValueError in float()
        "div 1 0",              # division by zero
        "hello",                # unknown command
        "add 2 2",              # valid command
        "exit"                  # exit
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    repl()
    out = capsys.readouterr().out

    # Assertions just to ensure output contains each branch's text
    assert "Usage:" in out
    assert "Error: Please provide two numbers" in out
    assert "Can't divide by zero." in out
    assert "Unknown command" in out
    assert "4.0" in out
    assert "Goodbye!" in out
