"""
## Lambda usage


Zasada jest prosta: Używaj w kolekcjach, jako argumenty ale nigdy nie przypisuj ich do zmiennych!
"""

users = [
    {"username": "developer", "priority": 0},
    {"username": "admin", "priority": 5},
    {"username": "jan_kowalski", "priority": 1},
    {"username": "tester", "priority": 0},
]

print(sorted(users, key=lambda x: x["priority"]))
print(list(map(lambda x: x["username"], users)))
print(list(filter(lambda x: x["priority"] == 0, users)))


from functools import reduce

numbers = [1, 6, 3, -5, 7, 9, -2]
print(sum(numbers))
print(reduce(lambda x, y: x + y if y > 0 else x, numbers))
