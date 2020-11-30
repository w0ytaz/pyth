"""
## Positional-Only Parameters

https://www.python.org/dev/peps/pep-0570
Python 3.8+
"""


def name(
    positional_only_parameters,
    # /,
    positional_or_keyword_parameters,
):
    ...


def position(x, y):  # , /):
    print(f"Position ({x},{y})")


position(1, 2)

"""
    > Position (1,2)
"""

position(x=1, y=2)
"""
    > TypeError: position() got some positional-only arguments passed as keyword arguments: 'x, y'
"""
