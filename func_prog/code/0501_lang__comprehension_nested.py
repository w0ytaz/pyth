"""
## Nested Comprehension
"""


[element for nested_list in [] for element in nested_list]


company = [
    {
        "z krakowa": [
            {"name": "Magdalena", "age": 20, "hobby": ["whiskey", "book", "tv"]},
            {"name": "Dżesika", "age": 27, "hobby": ["book", "wine"]},
        ],
        "z Warszawy": [
            {"name": "Wojtek", "age": 19, "hobby": ["football"]},
            {"name": "Kazimiera", "age": 23, "alc": ["wine"]},
        ],
    }
]


personel = [
    person for city in company for c, persons in city.items() for person in persons
]
print(personel)
"""
> [
    {"name": "Magdalena", "age": 20, "hobby": ["whiskey", "book", "tv"]},
    {"name": "Dżesika", "age": 27, "hobby": ["book", "wine"]},
    {"name": "Wojtek", "age": 19, "hobby": ["football"]},
    {"name": "Kazimiera", "age": 23, "alc": ["wine"]},
]
"""
