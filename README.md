# Sims 4 Scripting Boilerplate Project

This is a bolerplate project, sort of like a pre-made template and it represents one project so you can copy it for new 
projects. To get started just download, do some super quick setup, and you're ready to go. It can decompile the game 
libraries and compile your mod into 2 different flavors and don't forget to check back for occasional updates. 
Read more below.

I also wrote a full [tutorial here](https://medium.com/@junebug12851/the-sims-4-modern-python-modding-part-5-project-template-c9ffee48ab4e)

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
This provides 2 scripts currently `compile.py` and `decompile.py`.

### compile.py
This compiles your `src` folder and creates a `build` folder with 2 versions of your mod. A `slim` version and a `full` 
version. It then copies the slim version to your Sims 4 Mods folder removing the old one.

* The slim version contains only the compiled python files and that's it because that's all that the game needs. 
Therefore the slim version is, well, slim and small.
* The full version contains everything in your `src` folder. Whatever you place in there will be copied to the full 
version including the un-compiled code (source code). Next to all the source code, though, is an identical compiled 
code. This mod is not going to be slim, it's going to be more full and contain stuff the game doesn't need to run.

***If the game doesn't need all the stuff in the full version, why add it in there?*** The only reason you would want
to distribute the full version is if your thinking about the players who might want to open it up and look inside. With
the full version you can distribute a special license file next to the source code and even links, etc... This can allow
players to look inside, see the source code, maybe tinker with your mod, etc... Because it can promote learning and fun.

If you don't care about any of that then distribute the slim version because none of that stuff is in the slim version
and if the player opens a slim version they're just going to see compiled code and be unable to read it without using
a decompiler.

### decompile.py
I put a lot of work into this and this is a big area where mine greatly differs from `andrew`. It leverages the latest 
decompiler that has the highest success rate currently [uncompyle6](https://pypi.org/project/uncompyle6/) and goes 
through all the code in your game folder, decompiling them one-by-one placing them into a global projects folder.

Throughout the process it prints a pretty progress meter and at the end of each module it decompiled it shows the
success and fail stats as well as how long it took. It does this again at the end of the whole decompilation. It also
clears out the old decompiled files for you and overall makes everything very smooth and simple.

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
