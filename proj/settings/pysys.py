from pathlib import Path
from proj.settings import cur_platform

import os
import sys

# Path to the running python executable
sys_path = sys.executable

# Path to the folder containing the running python executable
sys_folder_path = Path(sys_path).parent

# Path to the CTYPES folder (Used for Debugging)
sys_ctypes_path = os.path.join(sys_folder_path, "Lib", "ctypes")

# Path to the folder containing installed python modules
sys_scripts_path_windows = os.path.join(sys_folder_path, 'Scripts')
sys_scripts_path_darwin = os.path.join(sys_folder_path)

sys_scripts_path = ""
if cur_platform == "Windows":
    sys_scripts_path = sys_scripts_path_windows
else:
    sys_scripts_path = sys_scripts_path_darwin

sys_scripts_ext_windows = ".exe"
sys_scripts_ext_darwin = ""

sys_scripts_ext = ""
if cur_platform == "Windows":
    sys_scripts_ext = sys_scripts_ext_windows
else:
    sys_scripts_ext = sys_scripts_ext_darwin
