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

# core imports
import os
import fnmatch
import shutil
import tempfile
from zipfile import PyZipFile
from pathlib import Path

# Helpers
from Utility.helpers_path import replace_extension, get_rel_path, get_file_stem, ensure_path_created
from Utility.helpers_package import install_package, exec_package
from Utility.helpers_time import get_time, get_time_str, get_minutes

# Globals
script_package_types = ['*.zip', '*.ts4script']
python_compiled_ext = "*.pyc"

# Global counts and timings for all the tasks
total_suc_count = 0
total_fail_count = 0
total_count = 0
total_minutes = 0


def decompile_pre() -> None:
    """
    Here we ensure uncompyle6 is installed and install it if not
    We do this first because installation can create an error

    :return: Nothing
    """

    print("Checking for decompiler and installing if needed...")
    install_package("uncompyle6")


def decompile_dir(src_dir: str, dest_dir: str, filename: str) -> None:
    """
    Decompiles a directory of compiled python files to a different directory
    Modified from andrew's code.
    https://sims4studio.com/thread/15145/started-python-scripting

    :param src_dir: Path of dir to decompile
    :param dest_dir: Path of dir to send decompiled files to
    :param filename: Original filename of what's being decompiled (For progress output purposes)
    :return: Nothing
    """

    # Gain R/W to global counts and timing
    global total_suc_count
    global total_fail_count
    global total_count
    global total_minutes

    # Begin clock
    time_start = get_time()

    print("Decompiling " + filename)

    # Local counts for this one task
    col_count = 0
    suc_count = 0
    fail_count = 0
    count = 0

    # Go through each compiled python file in the folder
    for root, dirs, files in os.walk(src_dir):
        for filename in fnmatch.filter(files, python_compiled_ext):

            # Get details about the source file
            src_file_path = str(os.path.join(root, filename))
            src_file_rel_path = get_rel_path(src_file_path, src_dir)

            # Create destination file path
            dest_file_path = replace_extension(dest_dir + os.path.sep + src_file_rel_path, "py")

            # And ensures the folders exist so there's no error
            # Make sure to strip off the file name at the end
            ensure_path_created(str(Path(dest_file_path).parent))

            # Decompile it to destination
            success = exec_package("uncompyle6",
                                   "-o " + '"' + dest_file_path + '"' + " " +
                                   '"' + src_file_path + '"')

            # Print progress
            # Prints a single dot on the same line which gives a nice clean progress report
            # Tally number of files and successful / failed files
            if success:
                print(".", end="")
                suc_count += 1
                total_suc_count += 1
            else:
                print("x", end="")
                fail_count += 1
                total_fail_count += 1

            count += 1
            total_count += 1

            # Insert a new progress line every 80 characters
            col_count += 1
            if col_count >= 80:
                col_count = 0
                print("")

    time_end = get_time()
    elapsed_minutes = get_minutes(time_end, time_start)
    total_minutes += elapsed_minutes

    # Print a newline and then a compact completion message giving successful, failed, and total count stats and timing
    print("")
    print("")
    print("Completed")
    print("S: " + str(suc_count) + " [" + str(round((suc_count/count) * 100, 2)) + "%], ", end="")
    print("F: " + str(fail_count) + " [" + str(round((fail_count/count) * 100, 2)) + "%], ", end="")
    print("T: " + str(count) + ", ", end="")
    print(get_time_str(elapsed_minutes))
    print("")


def decompile_zip(src_dir: str, filename: str, dst_dir: str) -> None:
    """
    Copies a zip file to a temporary folder, extracts it, and then decompiles it to the projects folder
    Modified from andrew's code.
    https://sims4studio.com/thread/15145/started-python-scripting

    :param src_dir: Source directory for zip file
    :param filename: zip filename
    :param dst_dir: Destination for unzipped files
    :return: Nothing
    """

    # Create paths and directories
    file_stem = get_file_stem(filename)

    src_zip = os.path.join(src_dir, filename)
    dst_dir = os.path.join(dst_dir, file_stem)

    tmp_dir = tempfile.TemporaryDirectory()
    tmp_zip = os.path.join(tmp_dir.name, filename)

    # Copy zip to temp path
    shutil.copyfile(src_zip, tmp_zip)

    # Grab handle to zip file and extract all contents to the same folder
    zip = PyZipFile(tmp_zip)
    zip.extractall(tmp_dir.name)

    # Decompile the directory
    decompile_dir(tmp_dir.name, dst_dir, filename)

    # There's a temporary directory bug that causes auto-cleanup to sometimes fail
    # We're preventing crash messages from flooding the screen to keep things tidy
    try:
        tmp_dir.cleanup()
    except:
        pass


def decompile_zips(src_dir: str, dst_dir: str) -> None:
    """
    Decompiles a folder of zip files to a destination folder
    Modified from andrew's code.
    https://sims4studio.com/thread/15145/started-python-scripting

    :param src_dir: Directory to search for and decompile zip files
    :param dst_dir: Directory to send decompiled files to
    :return: Nothing
    """
    for root, dirs, files in os.walk(src_dir):
        for ext_filter in script_package_types:
            for filename in fnmatch.filter(files, ext_filter):
                decompile_zip(root, filename, dst_dir)


def decompile_print_totals() -> None:
    print("Results")

    # Fix Bug #1
    # https://github.com/junebug12851/Sims4ScriptingBPProj/issues/1
    try:
        print("S: " + str(total_suc_count) + " [" + str(round((total_suc_count / total_count) * 100, 2)) + "%], ", end="")
        print("F: " + str(total_fail_count) + " [" + str(round((total_fail_count / total_count) * 100, 2)) + "%], ", end="")
        print("T: " + str(total_count) + ", ", end="")
        print(get_time_str(total_minutes))
    except:
        print("No files were processed, an error has occurred. Is the path to the game folder correct?")
        pass

    print("")
