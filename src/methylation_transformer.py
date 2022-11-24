#!/usr/bin/python3
"""
This script extracts methylations

Required:
    - Python >= 3.6

=========================
"""

# -*- coding: utf-8 -*-
__author__ = "{ThankGod Ebenezer}"

import os.path

# Built-in/generic imports

# Futures and third party libraries

# Futures local application libraries, source package
from addscriptdir2path import add_package2env_var
from package.commandlineoperations.commandlineoperator import CommandLineOperator
from package.dataframeoperations.write_out_dataframes import DataFrameWriter
from package.fileoperations.filehandlers import FileHandler
from package.lateralprocessing.parallelprocessing import synchronize_processes_pathos
from package.logprocesses.logprocesses import change_logging_format
from package.methylationextractionoperations.methylationextractionoperations import extract_methylations
from package.profiling.profiling import begin_profiling, end_profiling, ProfileLogger

# re-define system path to include modules, packages,
# and libraries in environment variable
add_package2env_var()


# logging
change_logging_format()

# profiling begins ###
profiling_starting = begin_profiling()


# main function
def main() -> None:
    """main function to run commandline arguments and call other functions to run."""

    cli_args_values = CommandLineOperator.get_cli_input_arguments()
    path_to_out_file = cli_args_values.path2out_file
    path_to_bam_files = cli_args_values.path2bam_files
    number_cpus = cli_args_values.num_cpus

    assert (os.path.exists(path_to_bam_files) and os.path.isdir(path_to_bam_files)), "supply an absolute path " \
                                                                                     "directory to -i"

    all_bed_graph_files = FileHandler.globally_get_all_files(path_to_bam_files, "_CpG.bedGraph")

    extracted_methylation_dataframe_df = synchronize_processes_pathos(
        extract_methylations,
        all_bed_graph_files,
        number_cpus,
    )

    DataFrameWriter.write_dataframe(extracted_methylation_dataframe_df, path_to_out_file)


###################################################################################
#run system argument ##############################################################
###################################################################################
if __name__ == "__main__":
    main()

time_end = end_profiling()
ProfileLogger(profiling_starting, time_end).log_profiling()
