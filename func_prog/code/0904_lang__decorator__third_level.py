"""
## Third level decorators
"""


def create_decorator(prefix="", postfix=""):
    def decorator(func):
        print(f"{prefix}Run {func.__name__} function{postfix}")

        def inner(*args, **kwargs):
            print(f"{prefix}With args:{args} and kwargs:{kwargs}{postfix}")
            return func(*args, **kwargs)

        return inner

    return decorator


def printer(x):
    print(x.upper())


create_decorator(prefix=":) ")(printer)("text\n")
"""
:) Run printer function
:) With args:('text\n',) and kwargs:{}
TEXT
"""


@create_decorator(prefix=">>")
def printer(x):
    print(x.upper())


printer("text\n")
"""
>>Run printer function
>>With args:('text\n',) and kwargs:{}
TEXT
"""
