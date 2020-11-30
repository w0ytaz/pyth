"""
# Generator
"""


def get_some_data():
    for x in "uh57a39fsg":
        if x.isalpha():
            yield x.upper()
        print(f"last value: {x}")


print(get_some_data())
"> <generator object get_some_data at 0x7ff8fe8b93b8>"

for value in get_some_data():
    print(value)

"""
U
last value: u
H
last value: h
last value: 5
last value: 7
A
last value: a
last value: 3
last value: 9
F
last value: f
S
last value: s
G
last value: g
"""
