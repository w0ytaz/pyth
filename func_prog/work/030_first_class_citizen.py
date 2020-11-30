"""
Rozbuduj zbiór funkcji tak, aby móc wykonywać bardziej złożone działania matematyczne (
    mnożenie, dzielnie, dodawanie kilku liczb
)
Wprowadzane mogą być wyłącznie cyfry.
"""


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def collect(y, a, b):
    print(f"Run {y.__name__} function with {a} and {b}")
    return y(a, b)


map = {"+": add, "-": sub}


def calculate(calculation):
    ...
    return result


result = calculate("2+2")
assert result == 4, result

result = calculate("5*3")
assert result == 15, result

result = calculate("8/4")
assert result == 2, result

result = calculate("2+2+9-8")
assert result == 5, result
