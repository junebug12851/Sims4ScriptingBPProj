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
import os
from proj.util.run import exec_cmd


def install_package(settings, package: str, package_check: str = None) -> bool:
    """
    This installs a package if it doesn't exist

    Thank you bradgonesurfing
    https://stackoverflow.com/questions/57593111/how-to-call-pip-from-a-python-script-and-make-it-install-locally-to-that-script

    :param settings: Settings object to read settings from
    :param package: Package name to install
    :param package_check: Package name to check is installed, if none is provided defaults to package variable.
    :return: Successfully installed/already installed or failure to install
    """

    print("Checking to see if " + package + " is installed...")

    # Default to package if empty
    if not package_check:
        package_check = package

    success = False

    # Attempt to import and attempt to install if unable to import
    try:
        __import__(package_check)
        success = True
        print(package + " is already installed!")
    except:
        print(package + " not installed, installing now...")
        success = exec_cmd(settings.sys_path,
                           "-m",
                           "pip",
                           "install",
                           package)

        if success:
            print("Successfully installed!")
        else:
            print("Failed to install...")

    return success


def exec_package(settings, package: str, *args) -> bool:
    """
    Executes the cli version of an installed python package

    :param settings: Settings object to read settings from
    :param package: Package name to execute
    :param args: Arguments to provide to the package
    :return: Return code for failure or success
    """

    cmd = settings.sys_scripts_path + os.sep + package + settings.sys_scripts_ext
    return exec_cmd(cmd, *args)
