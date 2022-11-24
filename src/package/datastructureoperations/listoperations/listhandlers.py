"""
A collection of functions that performs list handling operations within a script.
"""

__name__ = "__main__"

# Built-in/generic imports
import sys
import logging

# Futures and third party libraries
from itertools import zip_longest
import pandas as pd


# Futures local application libraries, source package
from src.package.datastructureoperations.tupleoperations.tuplehandlers import append2tuple

# system modules, packages, libraries, and programs ###


def transform_listoflist2list(list_of_list: list) -> list:
    "transform a list of list to a list"

    one_dimensional_list = [
        second_list for first_list in list_of_list for second_list in first_list
    ]

    return one_dimensional_list


def add2listoftuples(list_of_tuples: list, item2append: str) -> list:
    """ adds a string, list, tuple or item to a list of tuples """

    listoftuples_tupled = [
        append2tuple(file_sppcode_nodename, item2append)
        for file_sppcode_nodename in list_of_tuples
    ]

    return listoftuples_tupled


def add_item2list(all_items: list, item2add: str) -> list:
    """ add an item to a list """

    if isinstance(item2add, str) is True or isinstance(item2add, int) is True:
        items_added = [element + [item2add] for element in all_items]

    elif isinstance(item2add, list):
        items_added = [element + item2add for element in all_items]

    return items_added


def add_list_elements2list(all_items: list, item2add: list) -> list:
    """ add a list item to a list """

    single_item = get_first_element(all_items)

    if isinstance(item2add, list) is True and isinstance(single_item, list) is True:
        items_added = [element + item2add for element in all_items]
    elif (
        isinstance(item2add, list) is True
        and isinstance(single_item, pd.DataFrame) is True
    ):
        items_added = [[element] + item2add for element in all_items]

    elif isinstance(item2add, list) is True and isinstance(single_item, tuple) is True:
        items_added = [[element] + item2add for element in all_items]

    elif not isinstance(item2add, list) is True:
        assert (
            isinstance(item2add, list) is True
        ), """ second input, {}, to add_list_elements2list must be a list """.format(
            item2add
        )
    else:
        sys.exit("{} must be of data type list".format(all_items))

    return items_added


def list_is_not_empty(list_items: list) -> bool:
    """ checks if a list is empty """

    if len(list_items) > 0:
        list_status = True
    elif len(list_items) == 0:
        list_status = False

    return list_status


def list_is_gt_one(list_items: list) -> bool:
    """ checks if a list is empty """

    if len(list_items) > 1:
        list_status = True
    elif len(list_items) == 0:
        list_status = False
    elif len(list_items) == 1:
        list_status = False

    return list_status


def list_is_eq_two(list_items: list) -> bool:
    """ check that list item is equal to two """

    if len(list_items) == 2:
        list_status = True
    else:
        list_status = False

    return list_status


def list_is_eq_one(list_items: list) -> bool:
    """ checks if a list is empty """

    if len(list_items) == 1:
        list_status = True
    elif len(list_items) == 0 or len(list_items) > 1:
        list_status = False

    return list_status


def list_is_eq_five(list_items: list) -> bool:
    """ checks if a list has exactly five elements """

    if len(list_items) == 5:
        list_status = True
    elif len(list_items) != 5:
        list_status = False

    return list_status


def list_is_eq_nine(list_items: list) -> bool:
    """ checks if a list has exactly nine elements """

    if len(list_items) == 9:
        list_status = True
    elif len(list_items) != 9:
        list_status = False

    return list_status


def transpose_list_of_lists(list_of_list: list) -> list:
    """transposes list of list """
    transposed_longest = list(zip_longest(*list_of_list))

    return transposed_longest


def get_last_element(a_list_item: list) -> str:
    """ gets the last element of a list """
    last_element = a_list_item[-1]

    return last_element


def remove_last_element(r_list_item: list) -> str:
    """ removes the last element of a list """

    return r_list_item[:-1]


def get_second2last_element(b_list_item: list) -> str:
    """ gets the second to last element of a list """

    return b_list_item[-2]


def get_first_element(a_list_item: list) -> str:
    """ gets the last element of a list """

    return a_list_item[0]


def get4m_atleast_second_element(a_list_item: list) -> str:
    """ gets from at least element one of a list """

    return a_list_item[1:]


def get4m_atleast_third_element(a_list_item: list) -> str:
    """ gets from at least element two of a list """

    return a_list_item[2:]


def second_element(a_list_item: list) -> str:
    """ gets second element"""

    return a_list_item[1]


def third_element(b_list_item: list) -> str:
    """ gets third element"""

    return b_list_item[2]


def get_fourth_element(b_list_item: list) -> str:
    """ gets fourth element"""

    return b_list_item[3]


def get_fifth_element(c_list_item: list) -> str:
    """ gets fifth element"""

    return c_list_item[4]


def get_sixth_element(d_list_item: list) -> str:
    """ gets sixth element"""

    return d_list_item[5]


def get_seventh_element(d_list_item: list) -> str:
    """ gets seventh element"""

    return d_list_item[6]


def get_eigth_element(d_list_item: list) -> str:
    """ gets eigth element"""

    return d_list_item[7]


def get_nineth_element(d_list_item: list) -> str:
    """ gets nineth element"""

    return d_list_item[8]


def convert2string(contents: list) -> list:
    """ converts all elements of a list to string """

    return [str(element) for element in contents]


def remove_empty_list(all_elements: list) -> list:
    """ removes empty list """

    return [
        element for element in all_elements if list_is_not_empty(element)
    ]


def transform_unknown_listoflist2list(list_items_two: list) -> list:
    """ transforms a possible list of list with unknown element types"""
    list_items_two_new = list(filter(None, list_items_two))

    list_level_status = [
        element_set
        for element_set in list_items_two_new
        if element_set is not None and list_is_not_empty(list(element_set)) is True
    ]

    list_containing_str = [
        element_one
        for element_one in list_items_two_new
        if element_one is not None and isinstance(element_one, str) is True
    ]

    if (
        list_is_not_empty(list_level_status) is True
        and list_is_not_empty(list_containing_str) is False
    ):
        list_level_status_tranformed = transform_listoflist2list(list_items_two_new)

    elif list_is_not_empty(list_containing_str) is True:
        list_level_status_tranformed = list_items_two_new

    elif list_is_not_empty(list_level_status) is False:
        list_level_status_tranformed = []

    return list_level_status_tranformed


def inner_intersect(content_one: list, content_two: list) -> list:
    """ find the intersect of two list """

    common_elements = [
        element_one
        for element_one in content_one
        for element_two in content_two
        if element_one == element_two
    ]

    return common_elements


def get_all_1st_elements_of_listoflist(a_listof_list: list) -> list:
    """ gets all the first elements of a list of list"""

    all_first_elements = [
        get_first_element(element)
        for element in a_listof_list
        if element is not None and list_is_not_empty(element) is True
    ]

    return all_first_elements


def get_all_2nd_elements_of_listoflist(a_listof_list: list) -> list:
    """ gets all the second elements of a list of list"""

    all_second_elements = [
        second_element(element)
        for element in a_listof_list
        if element is not None and list_is_not_empty(element) is True
    ]

    return all_second_elements
