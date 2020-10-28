#    Copyright 2020 June Hanabi
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

# Make sure you Open PyCharm Pro and create a configuration using the "Python Debug Server" template
# Using these settings
# host: localhost
# port: 5678

# Before running game make sure you select the debug profile and run debug in the editor beforehand
# Run debug_teardown.py when done to uninstall the debug capability as it can slow down the game

from Utility.helpers_debug import debug_ensure_pycharm_debug_package_installed, debug_install_mod, debug_install_egg, \
    debug_teardown
from settings import mods_folder, debug_eggs_path, debug_cmd_mod_src_path, debug_cmd_mod_name, debug_capability_name, \
    debug_mod_subfolder

# Ensure PyCharm Pro debug package is installed
debug_ensure_pycharm_debug_package_installed()

# Install the debug mod and egg
# The mod creates a cheat "pycharm.debug" which activates the debug process
# The egg injects the code into the game so that the debug process can happen
debug_teardown(mods_folder, debug_mod_subfolder)
debug_install_mod(debug_cmd_mod_src_path, mods_folder, debug_cmd_mod_name, debug_mod_subfolder)
debug_install_egg(debug_eggs_path, mods_folder, debug_capability_name, debug_mod_subfolder)

print("")
print("Complete!")
print("")
print("Step 1: Create a 'Python Debug Server' configuration In PyCharm Pro from the template using")
print("        IDE host name: localhost")
print("        port: 5678")
print("Step 2: Select debug profile and begin debugging")
print("Step 3: Load up a playable lot in the game")
print("Step 4: Enter the cheatcode 'pycharm.debug'")
print("Step 5: Switch windows to the debugger and hit resume")
print("Step 6: The game and debugger are now connected, you're ready to start debugging!")
print("")
print("When you're done debugging, run 'debug_teardown.py' to uninstall the debugging capability. Otherwise leaving")
print("it in just makes your game slower")
