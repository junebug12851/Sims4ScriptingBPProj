import os

# Folder that contains global files for all projects
from proj.settings import projects_path

# Name of the folder in the projects folder that will contain built files and other game files like Tuning files
projects_lib_folder = "__util"

# Variables that depend on other variables need to be enclosed in a function so that if the user overrides the variables
# the changes will be reflected.


def projects_python_subpath() -> str:
    """
    Subpath to extracted python files from the game to the projects folder
    """

    return projects_lib_folder + os.sep + "Python"


def projects_tuning_subpath() -> str:
    """
    Subpath to extracted tuning files from the game to the projects folder
    """

    return projects_lib_folder + os.sep + "Tuning"


def projects_python_path() -> str:
    """
    Full path to extracted python files from the game to the projects folder
    """

    return os.path.join(projects_path, projects_python_subpath())


def projects_tuning_path() -> str:
    """
    Full path to extracted tuning files from the game to the projects folder
    """

    return os.path.join(projects_path, projects_tuning_subpath())
