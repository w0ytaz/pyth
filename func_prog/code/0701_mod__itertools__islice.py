"""
## Islice
"""

from itertools import islice

iterable = (x for x in range(100))
for num in islice(iterable, 15, 19):
    print(num)

"""
15
16
17
18
"""
