"""
## Example
"""

from datetime import datetime


def creation_date(obj):
    setattr(obj, "creation_date", datetime.now())

    obj.__str = obj.__str__
    obj.__str__ = lambda x: obj.__str(x) + f" # with creation_date"

    return obj


@creation_date
class User:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"User(name={self.name})"


u = User("Jarek")
print(dir(u))
print(u.creation_date)
print(u)
