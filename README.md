# IS601 - Assignment 3

Advanced Calculator with DRY principals

```bash
Welcome to Lakshya's Calculator
Available commands: add, sub, mul, div, exit
calc> 
```

#### Error handling in Division operation
```bash
calc> div 4 0
Traceback (most recent call last):
  File "/Users/lakshyasaharan/projects/IS601/module-3/IS601-assignment-3/main.py", line 8, in <module>
    repl()
    ~~~~^^
  File "/Users/lakshyasaharan/projects/IS601/module-3/IS601-assignment-3/calculator/repl.py", line 42, in repl
    result = Operations.division(x, y)
  File "/Users/lakshyasaharan/projects/IS601/module-3/IS601-assignment-3/calculator/operations.py", line 31, in division
    raise ValueError("Can't divide by zero.")
ValueError: Can't divide by zero.
```

#### Add operation
```bash
calc> add 2 3
5.0
```
#### Subtract operation
```bash
calc> sub 8 2
6.0
```

#### Multiply operation
```bash
calc> mul 7 4
28.0
```

#### Divide operation
```bash
calc> div 10 3
3.3333333333333335
```

#### Type *exit* to close
```bash
calc> exit
Goodbye!
```

## Setup

#### Clone my repo

```bash
git clone git@github.com:Lakshyasaharan5/IS601-assignment-3.git
```

#### Create a python venv and activate it

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Install packages from requirements.txt

```bash
pip install -r requirements.txt
```

#### Run pytest

```bash
pytest
```

## Github Actions for test

Github workflow has been implemented. When you push your code then Github Action will automatically test it using pytest.
