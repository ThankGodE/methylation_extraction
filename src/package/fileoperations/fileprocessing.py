"""a collection of classes and methods that read files """
from _csv import reader

import pandas as pd

from src.package.datastructureoperations.listoperations.listhandlers import get_first_element


class FileReader:
    """reads files"""

    @classmethod
    def convert_bed_graph_to_dataframe(cls, sam_file: str) -> pd.DataFrame:
        """converts a bedGraph file to dataframe. """

        return pd.read_csv(sam_file, sep='\t', header=None, skiprows=1, engine="python")




