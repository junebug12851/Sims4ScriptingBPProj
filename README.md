# Sims 4 Scripting Boilerplate Project

This is a bolerplate project, sort of like a pre-made template and it represents one project so you can copy it for new 
projects. To get started just download, do some super quick setup, and you're ready to go. It can decompile the game 
libraries and compile your mod into 2 different flavors and don't forget to check back for occasional updates. 
Read more below.

I also wrote a full [tutorial here](https://medium.com/@junebug12851/the-sims-4-modern-python-modding-part-5-project-template-c9ffee48ab4e)
and a separate [debug tutorial](https://medium.com/@junebug12851/the-sims-4-modern-python-modding-debugging-3736b37dbd9f)
covering the new automated debug capability.

## What this is
This is inspired from [andrew's tutorial](https://sims4studio.com/thread/15145/started-python-scripting) which is very 
popular and has helped many people, including me. I've modeled it after andrew's but want to go a different direction
with it entirely.

1. I've decided to make this into a proper open source project though on Github with
issue trackers, pull requests, version control etc... and I heavily documented the code.
2. I want this to be super easy and convenient to use but I want you to be able to understand it and have a place to ask
questions. I want to try my best to make it easily adaptable to the future so that when this goes out of date it can be
upgraded.
3. I want it to be editor agnostic. Not everyone wants to use PyCharm, it's nice, but it's also heavy and big and 
sometimes just more complicated than it needs to be. Some people don't use IDE's at all. Whatever works for you, I want
this project to fit that.

## Why I've waited so long before making this
In [part 1](https://levelup.gitconnected.com/the-sims-4-modern-python-modding-part-1-setup-83d1a100c5f6) of my tutorial
I described using Windows Powershell because the internet is full of old tutorials that have scripts which do everything
for you. While it sounds nice, it means you don't understand how those scripts work and by 2020 most of them are 5-6 
years out-of-date and some don't even run anymore. Other imposed a certain workflow which I have disagreements with and
you may as well or down the road.

I wanted to avoid also making another hands-off script that will become out of date and that doesn't teach you the rest
of the modding part which is packaging your mod and decompiling libraries but I get it, Power Shell scripts aren't that 
great workflow-wise so I've come to a compromise.

The takeaway point is that if I make a script that does everything for you then you're never going to learn how to do it
yourself and this is only going to act as a crutch down the line and hamper you instead of helping you. But given it's
importance to have I decided to make it anyways but keep it as well-written, documented, and detailed as much as 
possible as a compromise.

## What can it do
This provides several scripts you can run and use in your workflow and mod

### compile.py
This compiles and packages your `src` folder and creates a `build` folder containing your packaged mod ready for 
deployment. It then copies your packaged mod to the games Mods folder under it's own sub-folder 
`Mods/YourName_ProjectName/YourName_ProjectName.ts4script`.

**Update:**
The old behaviour was to create 2 mod files, a `slim` version and a `full` version. It no longer does this and opts to
only build a full version. The reason why is new information was learned about The Sims 4 loading process and it's
highly discouraged to only include compiled python files. I wrote a tutorial 
[about it here](https://medium.com/swlh/the-sims-4-modern-python-modding-ultimate-loading-guide-77ce1b68f1e7) detailing 
the reasoning behind this change.

### decompile.py
I put a lot of work into this and this is a big area where mine greatly differs from `andrew`. It leverages the latest 
decompiler that has the highest success rate currently [uncompyle6](https://pypi.org/project/uncompyle6/) and goes 
through all the code in your game folder, decompiling them one-by-one placing them into a global projects folder.

Throughout the process it prints a pretty progress meter and at the end of each module it decompiled it shows the
success and fail stats as well as how long it took. It does this again at the end of the whole decompilation. It also
clears out the old decompiled files for you and overall makes everything very smooth and simple.

### debug_setup.py and debug_teardown.py

These create and remove a debugging environment so that you can debug your game with a real debugger. The only downside
is that it requires PyCharm Pro, which is a paid program that costs money. There's no other known way to do this. If
you have PyCharm Pro then this will access the debugging capability in it and create 2 mods.

* `pycharm-debug-capability.ts4script` which gives the Sims 4 capability to debug by connecting to PyCharm Pro
* `pycharm-debug-cmd.ts4script` which creates a cheat code `pycharm.debug` you can enter in-game which will active
debugging for the rest of the game.

Both the cheatcode and `debug_setup.py` give clear and well-written instructions informing you of what to do and how
to set it up or what to expect. I've also written a 
[tutorial](https://medium.com/analytics-vidhya/the-sims-4-modern-python-modding-debugging-3736b37dbd9f) on how to
use it.

As the instructions say, run `debug_teardown.py` when not debugging because it can otherwise slow down your game.
Sigma1202 is the person who discovered this, I just made it into a script.

### devmode.py

This enters into a special mode called "Dev Mode", it clears out compiled code and links your src folder to the 
Mod Folder. When Dev Mode is activated, you don't need to compile anymore. If you run `compile.py` though it will exit 
Dev Mode and do a normal compile.

When inside of Dev Mode you can enter the cheat `devmode.reload [path.to.module]`, it'll reload the file live while
the game is running so it doesn't need to be closed and re-opened. For example, to reload main.py enter 
`devmode.reload main`. You can also enter paths to folders which will reload the entire folder or just not specify a 
path which will reload the entire project.

This only works in devmode.

### fix_tuning_names.py

This expects you to have extracted the tuning files from `Sims 4 Studio` with the `Sub-Folders` option checked. What 
this does is go through each and every tuning file and rename it to a much cleaner and better name.

For example:

```
From: "03B33DDF!00000000!0D94E80BE40B3604.sims.loan_tuning.Tuning.xml"
To: "sims_loan_tuning.xml"
```

Vastly prettier and cleaner don't you agree?

### sync_packages.py

Running this script searches the top-level assets folder for any `.package` files and then copies them to your
Mod Name Folder alongside your scripts. It's automatically run with `compile.py` and `devmode.py` and you can run it
anytime yourself.

### bundle_build.py

Zips up the build artifacts in a way that can be sent to Sims 4 Players or Mod Websites. It nests all the build 
artifacts in a subfolder named `CreatorName_ProjectName`. This way the player can directly unzip your mod into the Mods
folder and it will all be self-contained in it's own folder.

### cleanup.py

Removes all build artifacts

* The build folder
* The Mod Name folder in Mods
* Debug functionality

When completed, all traces of anything built by the project template for your mod will be removed leaving a fresh slate.
This is common when you just want to clean everything up, especially after your all done developing and want to
essentially "Un-Build" and "Un-Make" everything.

### src/helpers/injector.py

This uses the popular injector, brought to my attention by LeRoiDesVampires and TURBOSPOOK. It's widely used in the Sims
modding community across mods and tools. Reference it in your code to automate replacing functions in-game in a much
prettier way with less coding. Optional to use.

## How to get started with this

1. Download it to your computer wherever you like, this will be your project folder for one project.
2. Rename the folder to the name of your project.
3. Copy settings.py.orig to another file called settings.py, this will become your personal settings
3. Change the settings to match your username or display name and where different folders are on your computer.
4. If you don't already have the library decompiled, run `decompile.py` which will take a long time
5. Using your favorite editor whether it be `Sublime`, `Notepad++`, `Visual Studio Code`, `PyCharm`, or wherever begin
adding files to the `src` folder. 
6. Run `compile.py` and test it out. Keep making changes until you're happy then your done. If you want to publish your 
work you can publish slim, full, or both version.

## Settings

The toolkit has many settings found in `settings.py` and many of them you won't need to change but it's important that 
be the first place you go to before you start running scripts.

`creator_name`

This is the name you want prepended to the mod name.

`mods_folder`

This is where your sims 4 mods folder is location. It defaults to `Documents/Electronic Arts/The Sims 4/Mods`. It
automatically finds your Documents folder most of the time. 

**Note for Windows Users:** if you have moved your Documents folder to another drive then settings will not be
able to correctly locate it and you'll run into issues. In this case you would need to set it's location.

**Note for non-windows users** you may have to change this

`projects_folder`

This is where you have all of your Sims 4 Projects, it defaults to `Documents/Sims 4 Projects` again auto-finding your
Documents folder.

**Note for Windows Users:** if you have moved your Documents folder to another drive then settings will not be
able to correctly locate it and you'll run into issues. In this case you would need to set it's location.

**Note for non-windows users** you may have to change this

`game_folder`

This is where your game is installed. It defaults to `C:\Program Files (x86)\Origin Games\The Sims 4`. If this is not 
your location you need to change this.

**Note for non-windows users** you may have to change this

There are many other settings related to the project but you generally won't need to change them. I suggest going 
through the file though and making sure everything is how you want it.

## License

Licensed [Apache2](https://www.apache.org/licenses/LICENSE-2.0), basically do whatever you want to do as long as you 
credit me back and don't try to pose as me.

## Contributing

Contributions are welcome, just fork and send a pull request
