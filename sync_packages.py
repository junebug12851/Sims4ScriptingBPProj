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

# This installs, updates, and removes package files in the projects folder to match the assets folder
import fnmatch

import os
import shutil
from settings import assets_path, mods_folder, creator_name, project_name
from Utility.helpers_path import ensure_path_created, remove_file

mod_name_folder_path = mods_folder + os.sep + creator_name + "_" + project_name

ensure_path_created(mod_name_folder_path)

files_added = 0
file_list_failed = []

# Remove existing package files
for root, dirs, files in os.walk(mod_name_folder_path):
    for filename in fnmatch.filter(files, "*.package"):
        remove_file(root + os.sep + filename)

    # Only cover the top-level folder
    break

# Copy new package files to Mod Folder
for root, dirs, files in os.walk(assets_path):
    for filename in fnmatch.filter(files, "*.package"):
        try:
            shutil.copy(root + os.sep + filename,
                        mod_name_folder_path + os.sep + filename)
            files_added+=1
        except:
            file_list_failed.append(root + os.sep + filename)

    # Only cover the top-level folder
    break

print("Updated: " + str(files_added) + " package(s)")

if len(file_list_failed) > 0:
    print("")
    print("Failed to copy these files, make sure the packages are named uniquely")
    print("")
    print("\n".join(file_list_failed))
