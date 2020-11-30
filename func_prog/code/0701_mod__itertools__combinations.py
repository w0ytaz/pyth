"""
## combinations
"""


from itertools import combinations, combinations_with_replacement


for comb in combinations(["X", "Y", "Z"], 2):
    print(comb)
"""
('X', 'Y')
('X', 'Z')
('Y', 'Z')
"""


for comb in combinations_with_replacement(["X", "Y", "Z"], 2):
    print(comb)
"""
('X', 'Y')
('X', 'Z')
('Y', 'Z')
('X', 'X')
('X', 'Y')
('X', 'Z')
('Y', 'Y')
('Y', 'Z')
('Z', 'Z')
"""
