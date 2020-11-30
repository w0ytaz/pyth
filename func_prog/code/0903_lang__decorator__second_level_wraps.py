"""
## Wraps

https://docs.python.org/3.9/library/functools.html#functools.wraps
"""


from functools import wraps


def decorator(func):
    print(f"Run {func.__name__} function")

    @wraps(func)
    def inner(*args, **kwargs):
        print(f"With args:{args} and kwargs:{kwargs}")
        return func(*args, **kwargs)

    return inner


@decorator
def add_two(arg):
    return 2 + arg


add_two
"> <function add_two at 0x7fde7d96fc10>"

print(add_two.__name__)
"> add_two"
