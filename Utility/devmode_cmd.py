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
import fnmatch

from pathlib import Path

import os
import sims4.commands
from sims4.reload import reload_file


def reload_folder(path: str) -> None:
    """
    Reloads all the python files in a folder and all sub-folders

    :param path: Folder to reload
    :return: Nothing
    """

    for root, dirs, files in os.walk(path):
        for filename in fnmatch.filter(files, "*.py"):
            reload_file(root + os.sep + filename)


@sims4.commands.Command('devmode.reload', command_type=sims4.commands.CommandType.Live)
def _devmode_reload(module: str = "", _connection: int = None) -> None:
    """
    Provides functionality to reload a module while in devmode

    Type in:
    devmode.reload [path.of.module] to reload the module

    :param module: Path of the module to reload
    :param _connection: Provided by the game
    :return: Nothing
    """

    # Get ability to write to the cheat console and build path to project folder
    output = sims4.commands.CheatOutput(_connection)
    project_folder = str(Path(__file__).parent.parent)

    # Stop here if a module path wasn't given, in this case reload the whole project
    if not module:
        reload_folder(os.path.join(project_folder, "Scripts"))
        output("Reloaded entire project")
        return

    # Convert module path to a path and build a reload path
    sub_path = module.replace(".", os.sep)
    reload_path = os.path.join(project_folder, "Scripts", sub_path)

    # If it's a folder that exists reload the whole folder
    if os.path.exists(reload_path):
        if os.path.isdir(reload_path):
            reload_folder(reload_path)
            print("Reloaded Folder: " + sub_path)
            return
        else:
            print("Unknown file to reload" + sub_path)
            return

    # Assume it's a python file

    # If it doesn't exist then warn the user and stop here
    if not os.path.exists(reload_path + ".py"):
        output("Error: The file or folder doesn't exist to reload")
        output(sub_path + "[.py]")
        return

    # Issue the reloading and notify user
    reload_file(reload_path + ".py")
    output("Reloaded: " + sub_path + ".py")
