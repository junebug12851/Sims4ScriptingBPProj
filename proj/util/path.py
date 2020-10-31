#    Copyright 2020 June Hanabi
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

import os
import shutil
import glob
from pathlib import Path


def get_rel_path(path: str, common_base: str) -> str:
    """
    Returns path with common parent stripped out

    :param path: Path to strip out common parent
    :param common_base: Common parent
    :return: Path with common parent stripped out
    """
    return str(Path(path).relative_to(common_base))


def get_file_stem(file: str) -> str:
    """
    Returns file stem

    :param file: Filename with or without path
    :return: just the filename without extension
    """
    return Path(file).stem


def replace_extension(file: str, new_ext: str) -> str:
    """
    Replaces an extension from a path to another extension

    :param file: File path
    :param new_ext: New extension to replace with
    :return: New file extension
    """

    p = Path(file)
    return str(p.parent) + os.path.sep + p.stem + "." + new_ext


def get_full_filepath(folder: str, base_name: str) -> str:
    """
    This gets an absolute path to a file of an unknown extension

    Thank you Blender
    https://stackoverflow.com/questions/19824598/open-existing-file-of-unknown-extension?rq=1

    :param folder: Absolute path of file
    :param base_name: Name of file with unknown extension
    :return: Absolute path to file with extension
    """
    return glob.glob(os.path.join(folder, base_name + '.*'))[0]


def ensure_path_created(path: str) -> None:
    """
    Ensures folders are created and exist usually before doing work inside them
    Thank you Blair Conrad & Boris
    https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory

    :param path: The path to ensure exists
    :return: Nothing
    """
    Path(path).mkdir(parents=True, exist_ok=True)


def remove_dir(path: str) -> None:
    """
    Removes all folders and files in a directory
    Thank you Varun
    https://thispointer.com/python-how-to-delete-a-directory-recursively-using-shutil-rmtree/#:~:text=Delete%20all%20files%20in%20a,contents%20of%20a%20directory%20i.e.&text=It%20accepts%203%20arguments%20ignore_errors%2C%20onerror%20and%20path.

    :param path: Path to recursively remove
    :return: Nothing
    """

    # Uncomment if you want to turn on verification
    # a = input("Are you sure you want to remove the dir: " + path + " [yes/no]: ")
    # if a.lower() != "yes":
    #     sys.exit(1)

    # Remove folder and don't error out if it doesn't exist
    try:
        shutil.rmtree(path, ignore_errors=True)
    except:
        pass


def remove_file(path: str) -> None:
    """
    Removes a single file

    :param path: File to remove
    :return: Nothing
    """

    # Uncomment if you want to turn on verification
    # a = input("Are you sure you want to remove the file: " + path + " [yes/no]: ")
    # if a.lower() != "yes":
    #     sys.exit(1)

    # Remove file and don't error out if it doesn't exist
    try:
        os.remove(path)
    except:
        pass
