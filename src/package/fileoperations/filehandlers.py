"""
A collection of functions that performs file operations within a script.
"""

__name__ = "__main__"

# Built-in functions ###
import os
import glob


# classes, methods, and functions
class FileHandler:
    """class to handle files"""

    @classmethod
    def globally_get_all_files(cls, path2directory: str, file_extension=None) -> list:
        """gets all files in a directory if supplied with a path to all files
        e.g. (/path/to/file, 'fasta')"""

        if file_extension is None:
            all_files = glob.glob(path2directory + os.sep + "*")
        elif file_extension is not None:
            all_files = glob.glob(
                path2directory + os.sep + "**" + os.sep + "*" + file_extension,
                recursive=True,
            )

        return FileHandler.__decode_bom(all_files)

    @classmethod
    def __decode_bom(cls, all_path2file: list) -> list:
        """ decodes BOM i string """

        all_files_bom_decoded = [
            file.encode().decode("utf-8-sig") for file in all_path2file
        ]

        return all_files_bom_decoded

