"""
## Second level decorators
"""


def decorator(func):
    print(f"Run {func.__name__} function")

    def inner(*args, **kwargs):
        print(f"With args:{args} and kwargs:{kwargs}")
        return func(*args, **kwargs)

    return inner


def printer(x):
    print(x.upper())


decorator(printer)("text\n")


@decorator
def printer(x):
    print(x.upper())


printer("text\n")

printer
"> <function decorator.<locals>.inner at 0x7f7cc66338b0>"

print(printer.__name__)
"> inner"
