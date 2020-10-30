from pathlib import Path

import os
from proj.settings import project_mods_subpath, pycharm_pro_path

internal_mods_folder = "Sims4BPProject"

mod_debug_cmd_build_name = "pycharm-debug-cmd"
mod_debug_capability_build_name = "pycharm-debug-capability"

mod_devmode_cmd_build_name = "devmode-cmd"


def mod_devmode_cmd_src_subpath():
    return project_mods_subpath() + os.sep + "devmode.py"


def mod_debug_cmd_src_subpath():
    return project_mods_subpath() + os.sep + "debug.py"


def mod_devmode_cmd_src_path():
    return os.path.join(Path(__file__).parent.parent.parent, mod_devmode_cmd_src_subpath())


def mod_debug_cmd_src_path():
    return os.path.join(Path(__file__).parent.parent.parent, mod_debug_cmd_src_subpath())


def debug_eggs_path():
    return os.path.join(pycharm_pro_path, "debug-eggs", "pydevd-pycharm.egg")
