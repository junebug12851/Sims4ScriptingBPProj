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
import shutil
from Utility.helpers_debug import debug_teardown
from Utility.helpers_path import remove_dir
from Utility.helpers_symlink import symlink_remove_win
from settings import mods_folder, debug_mod_subfolder, creator_name, project_name, build_path

print("Removing Debug Setup...")
debug_teardown(mods_folder, debug_mod_subfolder)

print("Removing Mod Folder in Mods...")
symlink_remove_win(creator_name, mods_folder, project_name)

print("Removing Build folder...")
remove_dir(build_path)

print("")
print("Complete... All build artifacts have been removed!")
