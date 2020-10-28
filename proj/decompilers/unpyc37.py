import os

from pathlib import Path

import io
import sys

try:
    sys.path.insert(0, str(Path(__file__).parent) + os.sep + "unpyc37")
    import unpyc3
    UNPYC37_AVAILABLE = True
except:
    pass

def unpyc3_decompile(dest_file_path: str, src_file_path: str) -> bool:
    """
    Decompiles a python file via unpyc3

    :param dest_file_path: Path of the output file
    :param src_file_path:  Path of the source file to decompile
    :return: boolean to indicate whether it was successful or not
    """

    if not UNPYC37_AVAILABLE:
        return False

    try:
        suite = Utility.unpyc37.unpyc3.decompile(src_file_path)
        with io.open(dest_file_path, 'w') as output_file:
            for statement in suite.statements:
                output_file.write(str(statement))
                output_file.write(str('\n'))
    except Exception as e:
        return False

    return True
