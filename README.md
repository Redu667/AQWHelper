# Linux Console

A command-driven terminal interface for Linux. It runs inside a terminal and
does not require a graphical desktop, so it can be used from terminals running
under either X11 or Wayland.

## Run

```bash
./install.sh
```

The installer asks before creating the virtual environment, installing or
updating the app and its Python dependencies, adding the `aqwhelper` command
to `~/.local/bin`, and configuring Bash and Fish to include that directory in
`PATH`. It then offers to start the app in the current terminal. The installer
does not run in the background or open a separate desktop window. If you skip
shell configuration, you can still start it with
`~/.local/bin/aqwhelper`; open a new terminal after accepting PATH changes to
run `aqwhelper` from any directory.

The installer does not require administrator privileges. If virtual
environment creation fails on Debian or Ubuntu, install the system package
with `sudo apt install python3-venv` and run the installer again.

You can also start it without the installed command:

```bash
PYTHONPATH=src .venv/bin/python -m linux_console
```

The screen has two panels: `Info` lists the available commands, and the class
panel is titled with the current account name. Enter `char NAME` (for example,
`char Potato Lady`) to load a character; an optional leading slash is accepted.
Enter `char` without a name to show saved characters in the Info panel, then
click a name to load it and return to the Commands view. Use `char -NAME` to
remove a character from the saved list; removing the startup-default character
also clears it as the default.
Use `class NAME` to display any class in the Info panel, whether or not the
account owns it. Use `reload` (or `/rl`) to fetch the account's classes again, and
`return` (or `/r`) to return to the Commands home page. The class
list refreshes each time the app opens for the saved
character. Use `char NAME` to change the saved default. Settings are stored in
`$XDG_CONFIG_HOME/aqw-helper/config.json`, or `~/.config/aqw-helper/config.json`
when `XDG_CONFIG_HOME` is unset. On launch, the app silently checks the
version against the project's `main` branch. If a different version is found,
an update icon appears at the bottom of the Info panel; clicking it fills
`/update` into the command line without executing it. `/update` still asks for
confirmation, and automatic code synchronization is not configured yet. Close
the app with `Ctrl+C`.

Command aliases are `/ch` and `/character` for `/char`, `/rl` for `/reload`,
`/cl` and `/classes` for `/class`, `/up` for `/update`, and `/r` for `/return`.
Tab or Right Arrow
accepts the current completion suggestion; Up and Down cycle through saved
character names or class names with JSON data files. When no character history
exists, `/char` suggests `CHAR`.

Selecting a class opens a navigation view in the Info panel. Use its Back
button to move between the class, category, and detail screens. Enhancement
fields and skill/passive names are individually expandable to show their
details. The first time a class is opened, AQW Helper creates a JSON template
for it in
`$XDG_DATA_HOME/aqw-helper/classes/`, or
`~/.local/share/aqw-helper/classes/` when `XDG_DATA_HOME` is unset. Edit that
class's JSON file to add enhancement types and details, and skill names and
details; reopen the class in the app to see the edits. Enhancement entries have
`type` and `info` strings under `enhancements` → `Solo`/`Group`/`Ultra` →
`Class`/`Helm`/`Weapon`/`Cape`. The `skills` array contains five objects with
`name` and `info` strings. `passives` contains two objects by default and may
contain a third; each has `name` and `info` strings. Blank skill names display
as `Skill 1` through `Skill 5`, blank passive names as `Passive 1` and
`Passive 2`. The optional third passive appears only when its name or info is
filled in. A reusable JSON example is available at
[`templates/template.json`](./templates/template.json). Older class files are
upgraded with the two default passive fields when opened.

The character page renders its inventory with JavaScript, so its class spans
are not in the initial HTML. The app reads the character ID from the page,
requests AQ's inventory endpoint, and displays the returned class names without
rank suffixes. The interface uses a dark background, red command input, green
Info panel, blue class list, and red errors.

## Test

```bash
.venv/bin/python -m unittest discover -s tests -v
```
