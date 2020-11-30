"""
## groupby
"""


from itertools import groupby


things = [
    ("animal", "bear"),
    ("animal", "duck"),
    ("plant", "cactus"),
    ("vehicle", "speed boat"),
    ("vehicle", "school bus"),
]

for key, group in groupby(things, lambda x: x[0]):
    print(key, group, [e for e in group])
"""
animal <itertools._grouper object at 0x7fb94944c280> [('animal', 'bear'), ('animal', 'duck')]
plant <itertools._grouper object at 0x7fb9494a1100> [('plant', 'cactus')]
vehicle <itertools._grouper object at 0x7fb94944c280> [('vehicle', 'speed boat'), ('vehicle', 'school bus')]
"""
