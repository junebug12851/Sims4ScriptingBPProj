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
from Utility.helpers_debug import debug_install_mod
from Utility.helpers_symlink import symlink_create_win, symlink_exists_win
from settings import mods_folder, src_path, creator_name, project_name, devmode_cmd_mod_src_path, devmode_cmd_mod_name

is_devmode = symlink_exists_win(creator_name, mods_folder, project_name)

if is_devmode:
    print("You're already in Dev Mode")
    raise SystemExit(1)

try:
    symlink_create_win(creator_name, src_path, mods_folder, project_name)
    debug_install_mod(devmode_cmd_mod_src_path, mods_folder, devmode_cmd_mod_name, creator_name + "_" + project_name)
    exec(open("sync_packages.py").read())
except:
    print("An error occurred!")
    pass
