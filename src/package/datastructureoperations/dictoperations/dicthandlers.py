"""
A collection of functions that performs tuple handling operations within a script.
"""

__name__ = "__main__"

# Futures and third party libraries
import pandas as pd

# classes, methods, and functions
def convert_dicts2dataframe(dict_structures: dict) -> list:
    """ converts multiple key:values structures to DataFrame """
    df_of_multiple_dicts = [
        pd.DataFrame({key: values}) for key, values in dict_structures.items()
    ]

    return df_of_multiple_dicts


def get_key_wt_value(key_values: dict, value_of_interest: any) -> str:
    """ gets the key of a dictionary with the value pair """

    all_keys = [key for key, value in key_values.items() if value == value_of_interest]

    if len(all_keys) == 1:
        keys2return = all_keys[0]
    elif len(all_keys) > 1:
        keys2return = sorted(all_keys)[0]

    return keys2return
