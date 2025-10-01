"""
Calculator REPL for performing add, sub, mul and div
"""

from calculator.operations import Operations

def repl():
    print("Welcome to Lakshya's Calculator")
    print("Available commands: add, sub, mul, div, exit")

    while True:
        command = input("calc> ").strip().split()

        if not command:
            continue

        cmd = command[0].lower()

        if cmd == "exit":
            print("Goodbye!")
            break

        if cmd in ("add", "sub", "mul", "div"):
            if len(command) != 3:
                print("Usage: <command> num1 num2")
                continue

            try:
                x = float(command[1])
                y = float(command[2])
            except ValueError: 
                print("Error: Please provide two numbers")
                continue

            if cmd == "add":
                result = Operations.addition(x, y)
            elif cmd == "sub":
                result = Operations.subtraction(x, y)
            elif cmd == "mul":
                result = Operations.multiplication(x, y)
            elif cmd == "div":
                try:
                    result = Operations.division(x, y)
                except ValueError as e:
                    print(str(e))
                    result = None
                if result is None:
                    continue

            print(result)
        else:
            print("Unknown command. Type add, sub, mul, div, or exit.")
