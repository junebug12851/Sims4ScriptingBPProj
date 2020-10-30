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
mods_path = os.path.expanduser(
    os.path.join('~', 'Documents', 'Electronic Arts', 'The Sims 4', 'Mods')
)

# Location of folder to contain your projects
projects_path = os.path.expanduser(
    os.path.join('~', 'Documents', 'Sims 4 Projects')
)

# Location of the game folder
game_path_windows = os.path.join('C:', os.sep, 'Program Files (x86)', 'Origin Games', 'The Sims 4')
game_path_darwin = os.path.expanduser(os.path.join('~', 'Applications', 'The Sims 4.app', 'Contents'))

# Location of PyCharm Pro
pycharm_pro_path_windows = os.path.join('C:', os.sep, 'Program Files', 'JetBrains', 'PyCharm 2020.2.2')
pycharm_pro_path_darwin = os.path.expanduser(os.path.join('~', 'Applications', 'PyCharm 2020.app', 'Contents'))

# Pick between the default windows or mac game folder location
game_path = ""
if cur_platform == "Windows":
    game_path = game_path_windows
else:
    game_path = game_path_darwin

# ONLY FOR USERS OF PYCHARM PRO: Location of PyCharm Professional for debug setup
# You do not need to use PyCharm at all or the professional version, ignore this setting if you are not
# Pick between the default windows or mac PyCharm Pro folder location
pycharm_pro_path = ""
if cur_platform == "Windows":
    pycharm_pro_path = pycharm_pro_path_windows
else:
    pycharm_pro_path = pycharm_pro_path_darwin
