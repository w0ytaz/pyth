"""
## First level decorators
"""


def printer(x):
    print(x.upper())


printer("text\n")
"""
TEXT
"""


def decorator(func):
    print(f"Run {func.__name__} function")
    return func


decorator(printer)("text\n")
"""
Run printer function
TEXT
"""


@decorator
def printer(x):
    print(x.upper())


printer("text\n")
"""
Run printer function
TEXT
"""
