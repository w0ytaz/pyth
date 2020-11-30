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


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def collect(y, a, b):
    print(f"Run {y.__name__} function with {a} and {b}")
    return y(a, b)


map = {"+": add, "-": sub, "*": mul, "/": div}


def calculate(calculation):
    result, *rest = calculation
    result = int(result)
    for i in range(int(len(rest)/2)):
        sign, num = rest[2*i:2*i+2]
        result = collect(map[sign], result, int(num))
    return result


def calculate(calculation):
    result, *rest = calculation
    result = int(result)
    for sign, num in zip(rest[0::2], rest[1::2]):
        result = collect(map[sign], result, int(num))
    return result


def calculate(calculation):
    calc = iter(calculation)
    result = int(next(calc))
    try:
        while 1:
            result = collect(map[next(calc)], result, int(next(calc)))
    except StopIteration:
        return result
    return result


result = calculate("2+2")
assert result == 4, result

result = calculate("5*3")
assert result == 15, result

result = calculate("8/4")
assert result == 2, result

result = calculate("2+2+9-8")
assert result == 5, result
