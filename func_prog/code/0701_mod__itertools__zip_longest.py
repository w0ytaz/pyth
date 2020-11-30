"""
## zip_longest
"""

from itertools import zip_longest

for x, y in zip_longest([1, 2, 3], [4, 5, 6, 7, 8, 9]):
    print(x, y)

"""
1 4
2 5
3 6
None 7
None 8
None 9
"""
