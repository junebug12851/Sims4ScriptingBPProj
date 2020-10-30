# The decompilers to use
# This is in order from first attempt to last attempt
# After some testing from ssinakhot, it was determined this order is the best
# Only these 3 decompilers are currently supported
import os
from proj.settings import game_path, cur_platform

# Decompilers listed in order from most preferrred to least preferred. If a decompiler fails, the next one will be
# attempted. If all fail then the file will be marked as a failure.
# ssinakhot tested these decompilers and determined this order is the best for both speed and accuracy.
decompilers = ['unpyc3', 'decompyle3', 'uncompyle6']

# Variables that depend on other variables need to be enclosed in a function so that if the user overrides the variables
# the changes will be reflected.


def game_python_paths_windows() -> str:
    """
    Generates paths to python containing folders inside the game folder on Windows
    """

    return [
        os.path.join(game_path, 'Data', 'Simulation', 'Gameplay'),
        os.path.join(game_path, 'Game', 'Bin', 'Python')
    ]


def game_python_paths_darwin() -> str:
    """
    Generates paths to python containing folders inside the game folder on Mac
    """

    return [
        os.path.join(game_path, 'Data', 'Simulation', 'Gameplay'),
        os.path.join(game_path, 'Python')
    ]


def game_python_paths() -> str:
    """
    Generates paths to python containing folders inside the game folder on the current OS
    """

    if cur_platform == "Windows":
        return game_python_paths_windows()

    return game_python_paths_darwin()
