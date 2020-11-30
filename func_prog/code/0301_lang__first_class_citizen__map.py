"""
## Functions map



"""


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def collect(y, a, b):
    print(f"Run {y.__name__} function with {a} and {b}")
    return y(a, b)


string = "5+2"

map = {"+": add, "-": sub}

a, sign, b = string
result = map[sign](a, b)
print(f"{string}={result}")

string = "9-2"
a, sign, b = string
a, b = int(a), int(b)
result = collect(map[sign], a, b)
print(f"{string}={result}")

