"""
A collection of functions to extract methylations.
"""

__name__ = "__main__"

import os
import pathlib
import sys

import pandas as pd

from src.package.dataframeoperations.dataframeoperation import DataFrameOperator
from src.package.fileoperations.fileprocessing import FileReader


# system modules, packages, libraries, and programs ###


# define functions
def extract_methylations(absolute_path2sam_file: str) -> pd.DataFrame:
    """extract methylation information"""

    assert (os.path.isfile(absolute_path2sam_file)), "supply absolute path of a file that exists"

    base_filename = pathlib.Path(absolute_path2sam_file).stem.replace("_CpG", "")

    pd.set_option('display.max_columns', None)

    bed_file_content_df = FileReader.convert_bed_graph_to_dataframe(absolute_path2sam_file)
    bed_file_content_renamed_df = DataFrameOperator.rename_dataframe(bed_file_content_df)
    sample_name_reference_df = DataFrameOperator.add_sample_name_column(base_filename, bed_file_content_renamed_df)

    print( sample_name_reference_df, "" )

    sys.exit()

    return base_filename



