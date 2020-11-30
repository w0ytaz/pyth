"""
## Example
"""

math_functions = {}


def math_operation(sign):
    def wrapper(func):
        math_functions[sign] = func

    return wrapper


@math_operation("+")
def add(a, b):
    return a + b


@math_operation("-")
def sub(a, b):
    return a - b


@math_operation("*")
def multiply(a, b):
    return a * b


print(math_functions)
