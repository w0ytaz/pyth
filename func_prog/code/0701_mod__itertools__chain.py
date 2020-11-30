"""
## chain
"""


from itertools import chain

for element in chain([1, 2, 3], ["X", "Y", "Z"]):
    print(element)

"""
1
2
3
X
Y
Z
"""
