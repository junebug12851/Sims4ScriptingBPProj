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

import py_compile
import tempfile
import os
import shutil
from pathlib import Path
from zipfile import PyZipFile, ZIP_STORED

from Utility.helpers_path import get_sys_folder, get_rel_path, remove_file, replace_extension, remove_dir, \
    ensure_path_created
from Utility.helpers_package import install_package

# Thank you to Sigma1202 from https://www.youtube.com/watch?v=RBnS8m0174U
# for coming up with this process

# This follows Sigma1202 process
#
# PyCharm Professional provides an ability to insert debug capability into an external system and then tap into that
# ability.
#
# This is a 2 part process:
# Part 1) Install the debugging capability, this is located in an egg file, we must modify the egg and then properly
# install it as a mod so the game will load it and gain the ability to debug with PyCharm Pro
# Part 2) We must get the game to reach out to our editor, to do this Sigma1202 has come up with the idea of a cheat
# command. This command makes theg ame reach out to PyCharm Pro, initiate the debugging connection, and then you're
# ready to start debugging.
#
# The command I developed is 'pycharm.debug' and I've hopefully made all of this very easy for the end user.


def debug_ensure_pycharm_debug_package_installed() -> None:
    """
    Ensures the debugging package is installed as requested by PyCharm Pro

    :return: Nothing
    """

    print("Making sure you have the debugging package installed...")
    install_package("pydevd-pycharm~=202.7319.64")


def debug_install_mod(mod_src: str, mods_dir: str, mod_name: str, mod_folder_name: str) -> None:
    """
    Compiles and installs the mod which adds a cheat code so the user can setup the debugger in-game

    :param mod_src: Path to the script which does this
    :param mods_dir: Path to the users mod folder
    :param mod_name: Name of the mod
    :param mod_folder_name: Name of mod Subfolder
    :return: Nothing
    """

    print("Compiling and installing the cheatcode mod...")

    ensure_path_created(mods_sub_dir)

    # Get compiled path and compile mod
    mod_src_pyc = replace_extension(mod_src, "pyc")
    py_compile.compile(mod_src, mod_src_pyc)

    # Create mod at destination and add compiled file to it
    zf = PyZipFile(mod_path, mode='w', compression=ZIP_STORED, allowZip64=True, optimize=2)
    zf.write(mod_src_pyc, mod_name + ".pyc")
    zf.close()


def debug_install_egg(egg_path: str, mods_dir, dest_name: str, mod_folder_name: str) -> None:
    """
    Copies the debug egg provided by Pycharm Pro which adds the capability to make debugging happen inside of
    PyCharm Pro. A bit of work goes into this so it'll be much slower.

    :param egg_path: Path to the debug egg
    :param mods_dir: Path to the mods folder
    :param dest_name: Name of the mod
    :param mod_folder_name: Name of mod Subfolder
    :return:
    """

    print("Re-packaging and installing the debugging capability mod...")
    # Get egg filename and path

    ensure_path_created(mods_sub_dir)

    # Create temp directory
    tmp_dir = tempfile.TemporaryDirectory()
    tmp_egg = tmp_dir.name + os.sep + filename

    # Remove old mod in mods folder there, if it exists
    remove_file(mod_path)

    # Copy egg to temp path
    shutil.copyfile(egg_path, tmp_egg)

    # Extract egg
    # This step is a bit redundant but I need to copy over everything but one folder into the zip file and I don't
    # know how to do that in python so I copy over the zip, extract it, copy in the whole folder, delete the one
    # sub-folder, then re-zip everything up. It's a pain but it's what I know hwo to do now and Google's not much help
    zip = PyZipFile(tmp_egg)
    zip.extractall(tmp_dir.name)
    zip.close()

    # Remove archive
    remove_file(tmp_egg)

    # Copy ctype folder to extracted archive
    shutil.copytree(sys_ctypes_folder, tmp_dir.name + os.sep + "ctypes")

    # Remove that one folder
    remove_dir(tmp_dir.name + os.sep + "ctypes" + os.sep + "__pycache__")

    # Grab a handle on the egg
    zf = PyZipFile(mod_path, mode='w', compression=ZIP_STORED, allowZip64=True, optimize=2)

    # Add all the files in the tmp directory to the zip file
    for folder, subs, files in os.walk(tmp_dir.name):
        for file in files:
            archive_path = get_rel_path(folder + os.sep + file, tmp_dir.name)
            zf.write(folder + os.sep + file, archive_path)

    zf.close()

    # There's a temporary directory bug that causes auto-cleanup to sometimes fail
    # We're preventing crash messages from flooding the screen to keep things tidy
    try:
        tmp_dir.cleanup()
    except:
        pass


def debug_teardown(mods_dir: str, mod_folder_name: str) -> None:
    """
    Deletes the 2 mods, they technically cause the running game to slow down

    :param mods_dir: Path to mods directory
    :param mod_folder_name: Name of mod Subfolder
    :return: Nothing
    """

    print("Removing the debugging mod files...")
    remove_dir(mods_sub_dir)
