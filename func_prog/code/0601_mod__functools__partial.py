"""
## Partial
"""


from functools import partial


basetwo = partial(int, base=2)
basetwo.__doc__ = "Convert base 2 string to an int."

result = basetwo("10010")
"> 18"


printrr = partial(print, sep="", end="")

printrr("Jan", "Czech")
printrr("Kasia", "Wrona")
"> JanCzechKasiaWrona"
