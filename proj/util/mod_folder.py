from proj.util.devmode import devmode_remove_windows
from proj.util.path import remove_dir


def safely_remove_mod_folder(settings):
    if settings.cur_platform == "Windows":
        devmode_remove_windows(settings)

    remove_dir(settings.mods_subdir_path())
