"""
# Iterator
"""


data = "13423"
iterator = iter(data)
print(iterator)
"> <str_iterator object at 0x7fc6ead96040>"


print(next(iterator))
"> 1"

print(next(iterator))
"> 3"

print(next(iterator))
"> 4"

print(next(iterator))
"> 2"

print(next(iterator))
"> 3"

print(next(iterator))
"""
Traceback (most recent call last):
  File "/home/fox/Desktop/workshop/21_func_prog_adv/code/0801_lang__iterator.py", line 27, in <module>
    print(next(iterator))
StopIteration
"""
