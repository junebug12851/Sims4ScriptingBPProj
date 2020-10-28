import os

# Folder that contains global files for all projects
from proj.settings import projects_folder

projects_output_name = "__util"

# Subpath inside the projects folder to place decompiled python files
projects_python_subpath = projects_output_name + os.sep + "Python"
projects_tuning_subpath = projects_output_name + os.sep + "Tuning"

projects_python_path = os.path.join(projects_folder, projects_python_subpath)
projects_tuning_path = os.path.join(projects_folder, projects_tuning_subpath)
