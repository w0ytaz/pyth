"""
# Unpack



"""

a, b, c = [1, 2, 3]

# for _ in range(123):


imie, _, wiek = ["Adam", "Nowak", 19]
imie, *_ = ["Adam", "Nowak", 19]
*_, wiek = ["Adam", "Nowak", 19]

osoba = ["Adam", "Nowak", 19]
imie, nazwisko, wiek = osoba

# result, status = ({"data":{}}, True)
# if status:
#     ...
# else:
#     ...

x, y = {1: True, 2: False}

a, b = b, a
a, b = (b, a)

def foo():
    return None, True

>>> x, y = {1: True, 2: False}.items()
>>> x
(1, True)
>>> y
(2, False)