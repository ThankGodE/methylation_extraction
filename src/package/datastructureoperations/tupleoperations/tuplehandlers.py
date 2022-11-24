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


def add_tuple_elements2tuple(all_items: list, item2add: tuple) -> list:
    """ add a tuple item to a tuple list"""

    if isinstance(item2add, tuple) is True:
        items_added = [element + item2add for element in all_items]
    elif isinstance(item2add, str) is True:
        items_added = [element + (item2add,) for element in all_items]
    elif isinstance(item2add, list) is not True:
        assert (
            isinstance(item2add, list) is True
        ), """ second input, {}, to add_list_elements2list must be a list """.format(
            item2add
        )

    return items_added


def pair_up_wt_tuple(pairing_items_one: list, pairing_item: str) -> list:
    """ pairs up elements of a list and an item as a tuple """

    paired_elements = [(element, pairing_item) for element in pairing_items_one]

    return paired_elements
