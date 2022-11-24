"""
A collection of functions that operates on commandline options
"""

__name__ = "__main__"

import argparse
# Built-in/generic imports
import logging
from argparse import Namespace

from src.package.logprocesses.logprocesses import change_logging_format

# Futures local application libraries, source package
# from logprocesses.logprocesses import change_logging_format

# logging
change_logging_format()


# classes, methods, and functions
class CommandLineOperator:
    """ gets all commandline input arguments """

    script_progress_status = (
        """ getting and checking all commandline input arguments...\n"""
    )

    logging.info(script_progress_status)

    @classmethod
    def get_cli_input_arguments(cls, args=None) -> Namespace:
        """gets input arguments from the commandline interface"""

        parser = argparse.ArgumentParser(
            prog="methylation_extraction.py",
            usage=""" methylation_extraction.py
                    -o path2out """,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            description=(
                """
                This script extracts methylation information from a bam file

                Required:
                    - Python >= 3.6
                    - Pathos
                    - Pandas
                    - MethylDackel>=0.5.1
                    - HTSlib>=1.9
                """
            ),
        )
        parser.add_argument(
            "-o",
            "--path2out_file",
            help="absolute path to processed output file ",
            required=True,
        )
        parser.add_argument(
            "-i",
            "--path2bam_files",
            help="""absolute path (parent directory) to bam files""",
            required=True,
        )

        parser.add_argument(
            "-n",
            "--num_cpus",
            help="""number of cpus to use""",
            default=4,
        )

        return parser.parse_args(args)
