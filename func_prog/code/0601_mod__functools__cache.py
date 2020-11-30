"""
## Cache
"""

import functools

from functools import lru_cache

# from functools import cache  # python >= 3.9


@lru_cache
def factorial(n):
    print("|", end="")
    return n * factorial(n - 1) if n else 1


factorial(10)
"|||||||||||"
3628800

factorial(5)
""
120

factorial(12)
"||"
479001600
