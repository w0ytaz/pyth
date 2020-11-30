"""
Stwórz dekorator, którym zmierzysz czas działania funkcji.
Wykorzystaj do tego bibliotekę wbudowaną `time`.
"""


import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(time.time() - start)
        return result

    return wrapper


@timer
def long_func():
    for i in range(10000):
        for j in range(10000):
            i * j


long_func()
"5.131114482879639"
