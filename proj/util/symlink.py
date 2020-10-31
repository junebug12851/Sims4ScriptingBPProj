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
from proj.util.path import remove_dir, ensure_path_created
from proj.util.run import exec_cmd
from pathlib import Path

import os


def symlink_exists_win(settings) -> bool:
    """
    Checks to see if a Scripts folder or file exists inside the Mod Folder

    :param settings: Settings object to read settings from
    :return: Whether a "Scripts" file or folder does exist in the Mod Folder
    """

    return os.path.exists(settings.mods_subdir_scripts_path())


def symlink_remove_win(creator_name: str, mods_dir: str, mod_name: str = "Untitled") -> None:
    """
    Safely removes the Mod Name Folder
    /Mods/ModName/

    This is very critical! In order to use symlinks on Windows without requiring admin privs we have to use
    "Directory Junctions", it's a special type of symlink intended for different purposes but works for our case.
    However Python doesn't support Directory Junctions, in fact it can't tell the difference between a directory
    junction and a real folder, it thinks they're the same.

    This means if you don't safely remove the Scripts directory junction, the original source code files the dev is
    working on will be wiped out irrecoverably when doing a re-compile or a re-devmode-setup. In other words, the dev
    will forever lose all the files they were working on as part of their project unless they had a backup elsewhere.
    Their hard work vanishes before their eyes just like that.

    This is unnacceptable, to have a safety process in check, this function removes the mod folder, safely removing
    the scripts folder beforehand. If it's unable to it creates a crash so as to not proceed.

    Always use this function to remove the Mod Name Folder

    :param creator_name: Creator Name
    :param mods_dir: Path to the Mods Folder
    :param mod_name: Name of Mod
    :return: Nothing
    """

    # Build paths
    scripts_path = get_scripts_path(creator_name, mods_dir, mod_name)
    mod_folder_path = str(Path(scripts_path).parent)

    # Check whether the Scripts folder exists
    exists = symlink_exists_win(creator_name, mods_dir, mod_name)

    # Delete the Scripts folder and check whether it was successful
    success = exec_cmd("rmdir", '"' + scripts_path + '"')

    # If the Scripts folder exists but could not be deleted then print an error message and raise an exception
    if exists and not success:
        print("")
        print("Error: Scripts folder exists but can't be removed... Did you create a Scripts folder inside the Mod "
              "Folder at: ")
        print(scripts_path)
        print("If so, please manually delete it and try again.")
        print("")
        raise

    # Otherwise remove the directory
    remove_dir(mod_folder_path)


def symlink_create_win(creator_name: str, src_dir: str, mods_dir: str, mod_name: str = "Untitled") -> None:
    """
    Creates a symlink, it first wipes out the mod that may be there. When entering devmode, you don't compile anymore,
    so any compiled code needs to be removed.

    :param creator_name: Creator Name
    :param src_dir: Path to the source folder in this project
    :param mods_dir: Path to the Mods Folder
    :param mod_name: Name of Mod
    :return: Nothing
    """

    # Build paths
    scripts_path = get_scripts_path(creator_name, mods_dir, mod_name)
    mod_folder_path = str(Path(scripts_path).parent)

    # Safely remove folder with symlink
    symlink_remove_win(creator_name, mods_dir, mod_name)

    # Re-create folder
    ensure_path_created(mod_folder_path)

    # Create Scripts Folder as a Directory Junction
    exec_cmd("mklink",
             '/J ' +
             '"' + scripts_path + '" '
             '"' + src_dir + '"')

    print("")
    print("Dev Mode is activated, you no longer have to compile after each change, run devmode.reload [path.of.module]")
    print("to reload individual files while the game is running. To exit dev mode, simply run 'compile.py' which will")
    print("return things to normal.")
    print("It's recomended to test a compiled version before final release after working in Dev Mode")
    print("")
