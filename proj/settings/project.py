from pathlib import Path

import os

# Folder within this project that contains your python/script files
project_src_name = "src"

# Folder within this project that your mods will be built to
project_build_name = "build"

# To hold asset files like xml tuning files and packages
project_assets_name = "assets"

# Folder that contains the internal project/template files
project_internal_name = "proj"

# Full path to this project
project_path = str(Path(__file__).parent.parent.parent)

# Variables that depend on other variables need to be enclosed in a function so that if the user overrides the variables
# the changes will be reflected.


def project_mods_subpath() -> str:
    """
    The subpath of the mods folder within this project
    """

    return project_internal_name + os.sep + "mods"


def project_src_path() -> str:
    """
    The full path to the project source folder
    """

    return os.path.join(project_path, project_src_name)


def project_build_path() -> str:
    """
    The full path to the project build folder
    """

    return os.path.join(project_path, project_build_name)


def project_assets_path() -> str:
    """
    The full path to the project assets folder
    """

    return os.path.join(project_path, project_assets_name)
