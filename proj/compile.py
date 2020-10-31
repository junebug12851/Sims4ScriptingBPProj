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

# import core packages
import fnmatch
import os
import shutil
import py_compile
from proj.util.mod_folder import safely_remove_mod_folder
from proj.util.path import replace_extension, get_rel_path, remove_file, remove_dir, ensure_path_created
from proj.util.zip import get_zip_handle
from zipfile import PyZipFile, ZIP_STORED


def compile_folder(settings, comp_folder: str, zf: PyZipFile) -> None:
    """
    Compiles a full mod (Contains all files in source including python files which it then compiles
    Modified from andrew's code.
    https://sims4studio.com/thread/15145/started-python-scripting

    :param settings: Settings object to read settings from
    :param comp_folder: Directory to compile
    :param zf: Zip File Handle
    :return: Nothing
    """

    # Loop through every file in the source folder
    for folder, subs, files in os.walk(comp_folder):

        # Find all the python source files
        for filename in fnmatch.filter(files, '*' + settings.source_file_ext):
            # Build full paths to the py and future pyc file
            file_path_py = folder + os.sep + filename
            file_path_pyc = replace_extension(file_path_py, settings.compiled_file_ext[1:])

            # Generate a relative path to the pyc file
            rel_path_pyc = get_rel_path(file_path_pyc, comp_folder)

            # Compile the py file to pyc file
            py_compile.compile(file_path_py, file_path_pyc)

            # Copy the pyc file to the archive correctly nested
            zf.write(file_path_pyc, rel_path_pyc)

            # Remove compiled pyc file
            remove_file(file_path_pyc)

        # Now loop through all files in the source folder regardless of it's extension
        for filename in files:

            # Generate a relative path
            rel_path = get_rel_path(folder + os.sep + filename, comp_folder)

            # Copy it to archive
            zf.write(folder + os.sep + filename, rel_path)


def compile_and_package_src(settings) -> None:
    """
    Packages your mod into a proper mod file. It packages every file and folder in the src folder additioanlly
    compiling python files next to the uncompiled ones.

    Modified from andrew's code.
    https://sims4studio.com/thread/15145/started-python-scripting

    :param settings: Settings object to read settings from
    :return: Nothing
    """

    print("Clearing out old builds...")

    # Delete and re-create build and sub-folder in Mods
    safely_remove_mod_folder(settings)
    remove_dir(settings.project_build_path())

    ensure_path_created(settings.project_build_path())
    ensure_path_created(settings.mods_subdir_path())

    print("Re-building mod...")

    # Compile the entire src folder to a packaged file in build
    zf = get_zip_handle(settings.compile_mod_to_build_path())
    compile_folder(settings, settings.project_src_path(), zf)
    zf.close()

    # Copy it over to the mods folder
    shutil.copyfile(settings.compile_mod_to_build_path(), settings.compile_mod_to_mods_path())

    print("----------")
    print("Complete")
