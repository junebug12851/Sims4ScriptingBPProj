import os

# Folder that contains global files for all projects
from proj.settings import projects_path

projects_lib_folder = "__util"


def projects_python_subpath():
    return projects_lib_folder + os.sep + "Python"


def projects_tuning_subpath():
    return projects_lib_folder + os.sep + "Tuning"


def projects_python_path():
    return os.path.join(projects_path, projects_python_subpath())


def projects_tuning_path():
    return os.path.join(projects_path, projects_tuning_subpath())
