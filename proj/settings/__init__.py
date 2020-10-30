# import all individual settings files into the global namespace
import sys

from proj.settings.naming import *
from proj.settings.core_paths import *
from proj.settings.decompiling import *
from proj.settings.project import *
from proj.settings.projects import *
from proj.settings.mods import *
from proj.settings.compiling import *
from proj.settings.pysys import *

# Attempt to import user-overides, replacing defaults
try:
    sys.path.insert(0, Path(__file__).parent.parent.parent)
    from settings import *
    print("Found and using user settings file...")
except:
    print("Not using user settings file...")
    pass
