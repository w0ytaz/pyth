"""
## Keyword-Only Arguments

https://www.python.org/dev/peps/pep-3102
Python 3.0+
"""

def foo(name):
    print(name)


foo("Jarek")
foo(name='Jarek')


def name(positional_or_keyword_parameters, *, keyword_only_parameters):
    ...


def style(obj, *, color, size):
    print(f"style {obj} with color {color} and size {size}")


style(obj="hair", color="blonde", size="short")

"""
    > style hair with color blonde and size short
"""

style("hair", "black", "medium")
"""
    > TypeError: style() takes 1 positional argument but 3 were given
"""

style("hair")
"""
    > TypeError: style() missing 2 required keyword-only arguments: 'color' and 'size'
"""
