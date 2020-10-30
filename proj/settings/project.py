from pathlib import Path

import os

# Folder within this project that contains your python/script files
project_src_name = "src"

# Folder within this project that your mods will be built to
project_build_name = "build"

# To hold asset files like xml tuning files and packages
project_assets_name = "assets"

# Folder that contains the internal template files
project_internal_name = "proj"

project_path = str(Path(__file__).parent.parent.parent)


def project_mods_subpath():
    return project_internal_name + os.sep + "mods"


def project_src_path():
    return os.path.join(project_path, project_src_name)


def project_build_path():
    return os.path.join(project_path, project_build_name)


def project_assets_path():
    return os.path.join(project_path, project_assets_name)
