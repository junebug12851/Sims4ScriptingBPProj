import os
from proj.settings import mods_path, mod_name, project_build_path

compiled_ext = ".ts4script"

# Variables that depend on other variables need to be enclosed in a function so that if the user overrides the variables
# the changes will be reflected.


def mods_subdir_path() -> str:
    """
    Full path to the folder inside /Mods that will house the compiled project files
    """

    return os.path.join(mods_path, mod_name())


def compile_mod_to_build_path() -> str:
    """
    The full path to compile the mod to inside the project build dir
    """

    return os.path.join(project_build_path(), mod_name() + compiled_ext)


def compile_mod_to_mods_path() -> str:
    """
    The full path to compile the mod to inside the games mods folder
    """

    return os.path.join(mods_subdir_path(), mod_name() + compiled_ext)