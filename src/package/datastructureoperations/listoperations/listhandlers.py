"""
A collection of functions that performs list handling operations within a script.
"""

__name__ = "__main__"

# Futures local application libraries, source package

# system modules, packages, libraries, and programs ###


def list_is_not_empty(list_items: list) -> bool:
    """ checks if a list is empty """

    if len(list_items) > 0:
        list_status = True
    elif len(list_items) == 0:
        list_status = False

    return list_status


def get_first_element(a_list_item: list) -> str:
    """ gets the last element of a list """

    return a_list_item[0]












