import os
from proj.settings import project_mods_subpath

# Subfolder to place mods and capabilities in when needed by the user
mods_template_subfolder = "Sims4BPProject"

# Dev Mode
mod_devmode_cmd_src_subpath = project_mods_subpath + os.sep + "devmode.py"
mod_devmode_cmd_build_name = "devmode-cmd"

# The name of the mod which will start the Pycharm debugging when entered into the game
# ONLY FOR PYCHARM PRO USERS: If you're not using PyCharm Pro don't worry about this setting
mod_debug_cmd_src_subpath = project_mods_subpath + os.sep + "debug.py"
mod_debug_cmd_build_name = "pycharm-debug-cmd"
mod_debug_capability_build_name = "pycharm-debug-capability"

devmode_cmd_mod_src_path = os.path.join(Path(__file__).parent, devmode_cmd_mod_src)
debug_cmd_mod_src_path = os.path.join(Path(__file__).parent, debug_cmd_mod_src)
debug_eggs_path = os.path.join(pycharm_pro_folder, "debug-eggs", "pydevd-pycharm.egg")