"""
# Unpack



"""

a, b, c = [1, 2, 3]

imie, _, wiek = ["Adam", "Nowak", 19]
imie, *_ = ["Adam", "Nowak", 19]
*_, wiek = ["Adam", "Nowak", 19]

osoba = ["Adam", "Nowak", 19]
imie, nazwisko, wiek = osoba

x, y = {1: True, 2: False}

a, b = b, a
a, b = (b, a)
