from pathlib import Path

import os
from proj.settings import project_mods_subpath, pycharm_pro_path

# When the user activates certain modes like DevMode and/or Debug, this is the folder the files will be placed into
# It's like an internally used folder within the /Mods game folder.
internal_mods_folder = "Sims4BPProject"

# Name of built mod that triggers in-game debug
# .ts4script will automatically be appended
mod_debug_cmd_build_name = "pycharm-debug-cmd"

# Name of built mod that gives the game debug capability
# .ts4script will automatically be appended
mod_debug_capability_build_name = "pycharm-debug-capability"

# Name of built mod that triggers devmode reloading
mod_devmode_cmd_build_name = "devmode-cmd"

# Filename of the debug egg
debug_egg_filename = "pydevd-pycharm.egg"

# Variables that depend on other variables need to be enclosed in a function so that if the user overrides the variables
# the changes will be reflected.


def mod_devmode_cmd_src_subpath() -> str:
    """
    Generates a subpath to the source file for the DevMode Mod to be compiled and placed inside the game
    """

    return project_mods_subpath() + os.sep + "devmode.py"


def mod_debug_cmd_src_subpath() -> str:
    """
    Generates a subpath to the source file for the Debug Cmd Mod to be compiled and placed inside the game
    """

    return project_mods_subpath() + os.sep + "debug.py"


def mod_devmode_cmd_src_path() -> str:
    """
    Generates a full path to the source file for the Debug Cmd Mod to be compiled and placed inside the game
    """

    return os.path.join(Path(__file__).parent.parent.parent, mod_devmode_cmd_src_subpath())


def mod_debug_cmd_src_path() -> str:
    """
    Generates a full path to the source file for the Debug Cmd Mod to be compiled and placed inside the game
    """
    return os.path.join(Path(__file__).parent.parent.parent, mod_debug_cmd_src_subpath())


def debug_eggs_path() -> str:
    """
    Generates a full path to the Debug Capability Egg File provided by PyCharm Pro to be fixed and placed inside the
    game.
    """
    return os.path.join(pycharm_pro_path, "debug-eggs", debug_egg_filename)
