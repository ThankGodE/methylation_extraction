"""
A collection of functions that performs tuple handling operations within a script.
"""

__name__ = "__main__"

### system modules, packages, libraries, and programs ###


def append2tuple(element: tuple, item2append: str) -> tuple:
    """ add an item to a tuple """

    if isinstance(item2append, str):
        element_tupled = element + (item2append,)
    elif isinstance(item2append, tuple):
        element_tupled = element + item2append

    return element_tupled


