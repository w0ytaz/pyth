"""
## Cached Property
"""

from functools import cached_property  # python >= 3.8


class Prototype:
    def __init__(self):
        self.__prop = None

    @property
    def prop(self):
        if not self.__prop:
            self.__prop = map(lambda x: x.upper(), "operacje")
        return self.__prop


obj = Prototype()
print(obj.prop)
"> <map object at 0x7f33bffa8190>"
print(obj.prop)
"> <map object at 0x7f33bffa8190>"


class Prototype:
    @cached_property
    def prop(self):
        return map(lambda x: x.upper(), "operacje")


obj = Prototype()
print(obj.prop)
"> <map object at 0x7f87d8619d30>"
print(obj.prop)
"> <map object at 0x7f87d8619d30>"
