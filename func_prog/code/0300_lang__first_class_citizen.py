"""
# First Class Citizen

Czyli typ pierwszoklasowy, jest to obiekt który może być:
- przekazywany i zwracany z funkcji
- przechowywany w zmiennej i strukturach danych

"""


def add(a, b):
    return a + b


def collect(func, a, b):
    return func(a, b)


collect(add, 1, 2)
"> 3"

collect(add, add(1, 2), add(4, 6))
"13"


def sub(a, b):
    return a - b


collect(add, add(sub(8, 2), sub(10, 9)), add(sub(10, add(5, 4)), 6))
"> 14"
