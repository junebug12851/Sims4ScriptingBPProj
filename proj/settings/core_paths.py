import platform
import os

# Current platform
# Thanks Shital Shah
# https://stackoverflow.com/questions/1854/python-what-os-am-i-running-on/58071295#58071295
# "Windows", "Linux" or "Darwin"
cur_platform = platform.system()

# ####################################################
# Default Paths
# ####################################################

# Sims 4 mod folder location
mods_folder_all = os.path.expanduser(
    os.path.join('~', 'Documents', 'Electronic Arts', 'The Sims 4', 'Mods')
)

# Location of folder to contain your projects
projects_folder_all = os.path.expanduser(
    os.path.join('~', 'Documents', 'Sims 4 Projects')
)

# Location of the game folder
game_folder_windows = os.path.join('C:', os.sep, 'Program Files (x86)', 'Origin Games', 'The Sims 4')
game_folder_darwin = os.path.join('~', 'Applications', 'The Sims 4.app', 'Contents')

# PyCharm Pro Windows
pycharm_pro_windows = os.path.join('C:', os.sep, 'Program Files', 'JetBrains', 'PyCharm 2020.2.2')
pycharm_pro_darwin = os.path.join('~', 'Applications', 'PyCharm 2020.app', 'Contents')  # This is just a guess!!!!!!!

# Pick between the default windows or mac game folder location
game_folder = ""
if cur_platform == "Darwin":
    game_folder = game_folder_darwin
else:
    game_folder = game_folder_windows

# ONLY FOR USERS OF PYCHARM PRO: Location of PyCharm Professional for debug setup
# You do not need to use PyCharm at all or the professional version, ignore this setting if you are not
pycharm_pro = ""
if cur_platform == "Darwin":
    pycharm_pro = pycharm_pro_windows
else:
    pycharm_pro = pycharm_pro_darwin

# Default Mods and Projects folder to "all" since they're the same on Windows and Darwin
mods_folder = mods_folder_all
projects_folder = projects_folder_all
