"""
# Comprehension
"""


personel = [
    {"name": "Magdalena", "age": 20, "hobby": ["whiskey", "book", "tv"]},
    {"name": "Dżesika", "age": 27, "hobby": ["book", "wine"]},
    {"name": "Wojtek", "age": 19, "hobby": ["football"]},
    {"name": "Wojtek", "age": 19, "hobby": ["football"]},
    {"name": "Kazimiera", "age": 23, "alc": ["wine"]},
]


names = [person["name"] for person in personel]
print(names)
"> ['Magdalena', 'Dżesika', 'Wojtek', 'Wojtek', 'Kazimiera']"


uniq_names = {person["name"] for person in personel}
print(uniq_names)
"> {'Wojtek', 'Kazimiera', 'Magdalena', 'Dżesika'}"


name_age = {person["name"]: person["age"] for person in personel}
print(name_age)
"> {'Magdalena': 20, 'Dżesika': 27, 'Wojtek': 19, 'Kazimiera': 23}"


result = (person["name"] for person in personel)
print(result)
"> <generator object <genexpr> at 0x7ff7a6d82900>"


print(",".join(result))
"> Magdalena,Dżesika,Wojtek,Wojtek,Kazimiera"


print(",".join(person["name"] for person in personel))
"> Magdalena,Dżesika,Wojtek,Wojtek,Kazimiera"


hobby = [person["hobby"] for person in personel if "hobby" in person]
print(hobby)
"> [['whiskey', 'book', 'tv'], ['book', 'wine'], ['football'], ['football']]"
