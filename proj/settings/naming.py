# Your Name
from pathlib import Path

# Creator name used in building and packaging of your mod
creator_name = 'My Creator Name'

# The name of this project, by default it's setup to use the folder name containing the project
project_name = Path(__file__).parent.parent.parent.stem

# Variables that depend on other variables need to be enclosed in a function so that if the user overrides the variables
# the changes will be reflected.


def mod_name() -> str:
    """
    Builds a mod name from the creator and project name
    """

    return creator_name + '_' + project_name
