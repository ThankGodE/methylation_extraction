"""
A collection of functions that registers or logs processes
"""

__name__ = "__main__"

# Built-in/generic imports
import logging


# classes, methods, and functions
def change_logging_format():
    """change logging format"""
    logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.DEBUG)

    return logging
