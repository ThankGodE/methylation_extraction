""" a collection of classes to work on a dataframe"""
import pandas as pd

from package.datastructureoperations.listoperations.listhandlers import get_first_element


class DataFrameOperator:

    """performs dataframe operations"""

    @classmethod
    def rename_dataframe(cls, dataframe: pd.DataFrame) -> pd.DataFrame:
        """rename a dataframe transformed from bedGraph. Column names are as so:
        https://github.com/dpryan79/MethylDackel"""

        return dataframe.rename(columns={0: "chromosome", 1: "start", 2: "end", 3: "methyl_percent",
                                         4: "methylated_bases", 5: "unmethylated_bases"})

    @classmethod
    def add_sample_name_column(cls, sample_name: str, reference_dataframe: pd.DataFrame) -> pd.DataFrame:
        """add sample name column to an existing dataframe"""

        number_rows = get_first_element(reference_dataframe.shape)
        sample_name_list = [sample_name]*int(number_rows)

        sample_name_df = pd.DataFrame({"sample_name": sample_name_list})

        return pd.concat([sample_name_df, reference_dataframe], axis=1)
