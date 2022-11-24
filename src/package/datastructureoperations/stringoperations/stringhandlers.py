"""
A collection of functions that performs string handling operations within a script.
"""

__name__ = "__main__"

### system modules, packages, libraries, and programs ###


def pair_stringwithelements(path2pair: str, list_of_elements: list):
    """ Given a list of static or fixed elements, this function pairs up an
    external free string or input to the elements in the list"""

    elements_paired = [(path2pair, element) for element in list_of_elements]

    return elements_paired
