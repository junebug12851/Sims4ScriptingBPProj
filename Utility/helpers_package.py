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

from subprocess import run, PIPE, call, DEVNULL
from Utility.helpers_path import get_sys_path, get_sys_scripts_folder, get_full_filepath


def install_package(package: str) -> None:
    """
    This installs a package if it doesn't exist

    Thank you bradgonesurfing
    https://stackoverflow.com/questions/57593111/how-to-call-pip-from-a-python-script-and-make-it-install-locally-to-that-script

    :param package: Package name to ensure is installed
    :return: Nothing
    """
    # noinspection PyBroadException
    try:
        __import__(package)
    except:
        cmd = get_sys_path()
        args = "-m pip install " + package
        call(cmd + " " + args,
             stdout=DEVNULL,
             stderr=DEVNULL)


def exec_package(package: str, args: str) -> bool:
    """
    Executes the cli version of an installed python package

    :param package: Package name to execute
    :param args: Arguments to provide to the package
    :return: Return code for failure or success
    """

    cmd = get_full_filepath(get_sys_scripts_folder(), package)
    result = run(cmd + " " + args, capture_output=True, text=True)
    return (not str(result.stderr)) and (result.returncode == 0)
