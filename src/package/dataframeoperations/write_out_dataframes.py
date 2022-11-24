"""collection of classses and functions to write dataframes to csv"""
import logging
import os.path

import pandas as pd

from package.datastructureoperations.listoperations.listhandlers import list_is_not_empty


class DataFrameWriter:
    """writes dataframe to out"""

    @classmethod
    def write_dataframe(cls, dataframes: list, path2out_dir: str,) -> None:
        """writes to csv"""

        try:

            entropy_to_list = DataFrameWriter.__remove_none(list(dataframes))

            assert(list_is_not_empty(entropy_to_list) is True), "all elements passed are None"

            concatenated_df = pd.concat(entropy_to_list, axis=0).sort_values("sample_name")

        except ValueError:
            logging.exception("All objects passed were None.  Exiting...")

        else:

            absolute_path_to_out = os.path.join(path2out_dir, "all_samples_extracted.tsv")
            concatenated_df.to_csv(absolute_path_to_out, sep="\t", index=False, encoding="utf-8")

    @classmethod
    def __remove_none(cls, dataframe_lists: list) -> list:
        """removes all Nones in list"""

        return [dataframe for dataframe in dataframe_lists if isinstance(dataframe, pd.DataFrame) and dataframe.empty
                is False]
