"""
A collection of functions to extract methylations.
"""

__name__ = "__main__"

import os
import pathlib

import pandas as pd

from src.package.dataframeoperations.dataframeoperation import DataFrameOperator
from src.package.fileoperations.fileprocessing import FileReader


# system modules, packages, libraries, and programs ###


# define functions
def extract_methylations(absolute_path2bed_graph_file: str) -> pd.DataFrame:
    """extract methylation information"""

    assert (os.path.isfile(absolute_path2bed_graph_file)), "supply absolute path of a file that exists"

    base_filename = pathlib.Path(absolute_path2bed_graph_file).stem.replace("_CpG", "")

    bed_file_content_df = FileReader.convert_bed_graph_to_dataframe(absolute_path2bed_graph_file)
    bed_file_content_renamed_df = DataFrameOperator.rename_dataframe(bed_file_content_df)

    return DataFrameOperator.add_sample_name_column(base_filename, bed_file_content_renamed_df)



