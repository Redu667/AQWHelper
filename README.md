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

The screen has two panels: `Info` lists the available commands, and changes to
`Char: NAME` while a character is loaded. The right panel has `Classes` and
`Enhancements` tabs in its top frame; click either title to switch tabs.
The Info panel's Back and Home controls are also clickable in its top frame.
Mouse input stays enabled for clickable controls, so the terminal's normal
drag-to-select text behavior is unavailable while the app is running. On the
first launch, when no characters are saved, the app opens with a centered
`Character name` field; enter a name to save and load that character. After
that, enter
`char NAME` (for example, `char Potato Lady`) to
load a character; an optional leading slash is accepted.
Enter `char` without a name to show saved characters in the Info panel, then
click a name to load it and return to the Commands view. Use `char -NAME` to
remove a character from the saved list; removing the startup-default character
selects the most recently used remaining character as the startup character.
Use `class NAME` to display any class in the Info panel, whether or not the
account owns it. Use `reload` (or `/rl`) to fetch the account's classes again, and
`return` (or `/r`) to return to the Commands home page. The class
list refreshes each time the app opens for the saved
character. The last-used character and saved-character list are stored together
in `profiles.json` beside the settings file at
`$XDG_CONFIG_HOME/aqw-helper/` (or `~/.config/aqw-helper/` when
`XDG_CONFIG_HOME` is unset). Older character settings are migrated from
`config.json` automatically. Enhancement selections start fully enabled,
can be toggled in the `Enhancements` tab, and are saved per character as
individual JSON files in the `characters` subfolder. Enhancement names are
color-coded, with unlisted enhancements using a light orange accent. Optional
add-on combinations inherit the color of their default enhancement, such as
`Wizard Mana Vamp` using the Wizard color. The always-available defaults use
dark red for Fighter, dark green for Thief, dark blue for Wizard, white for
Healer, orange-brown for Spellbreaker, light brown for Hybrid, and pink for
Lucky.
On launch, the app silently checks the
version against the project's `main` branch. If a different version is found,
an `↓ Update Pending` button appears at the bottom of the Info panel; clicking
it fills `/update` into the command line without executing it. `/update` asks
for confirmation, then downloads and installs the latest published GitHub
release into the current Python environment and automatically restarts the app
after a successful update. To prevent downgrades, the updater refuses releases
whose tag is behind or unrelated to the latest `main` commit; publish a new
release with a new tag from the latest `main` commit. The repository must have
a published GitHub release for this command to install.
Close the app with `Ctrl+C` or `/quit` (alias `/q`). On startup and exit, AQW
Helper clears transient in-memory character and class data; saved character
settings and class JSON files are preserved.

Command aliases are `/ch` and `/character` for `/char`, `/rl` for `/reload`,
`/cl` and `/classes` for `/class`, `/up` for `/update`, and `/r` for `/return`;
`/enh` for `/enhancements`, `/st` for `/stats`, and `/q` for `/quit`.
`enhancements` opens a clickable list of enhancement descriptions from the
shared enhancement data, and `stats` opens clickable STR, DEX, VIT, INT, WIS,
and LUK entries whose descriptions can be filled in in `app.py`.
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
class's JSON file for local overrides. Tracked class defaults live in
`src/linux_console/class_templates/`, ship with the application, and are loaded
whenever class data is opened; nonblank values in a local class file override
the tracked defaults. Edit and commit those templates to share class setups
with the project. In displayed JSON descriptions, signed
tokens beginning with `+` are light green and tokens beginning with `-` are
light red; following characters in the same space-delimited token share that
color. Class enhancement choices are stored under `enhancements` →
`Base`/`Solo`/`Group`/`Special` → `Class`/`Helm`/`Weapon`/`Cape` →
`best` and `alternative`, with `base` nested under `alternative` as the final
fallback. Available Best and Alternative choices display together beneath
each slot heading; unavailable choices are omitted. If neither is owned, Base
displays with a red `(!)` marker. Each option can be expanded to show its
shared enhancement details. Each mode's `Potions` object has `Tonic`, `Elixir`,
and `Potion` text values, displayed as three labeled lines. The shared
enhancement descriptions are stored in the tracked catalog at
[`templates/enhancements.json`](./templates/enhancements.json). Edit that file
and commit it to share the descriptions through GitHub. It has separate
`enhancements`, `defaults`, and `addons` sections, each with a shared `info`
string for each name. The application loads this catalog directly in a source
checkout; the matching packaged copy is used when installed. The always-owned
defaults are Fighter, Wizard,
Healer, Thief, Hybrid, Spellbreaker, and Lucky. Add-ons such as Aweblast,
Spiral Carve, Mana Vamp, Health Vamp, and Powerword DIE are assumed available
and are not listed as per-character toggles. Existing class files migrate Solo
and Group unchanged, map Ultra to Special, copy the previous Solo setup into
Base, and convert backup/default choices and potion lists to the new format.
The `skills` array contains five objects with
`name` and `info` strings. `passives` contains two objects by default and may
contain a third; each has `name` and `info` strings. Blank skill names display
as `Skill 1` through `Skill 5`, blank passive names as `Passive 1` and
`Passive 2`. The optional third passive appears only when its name or info is
filled in. A reusable JSON example is available at
[`templates/template.json`](./templates/template.json). Older class files are
upgraded with the two default passive fields when opened; their existing
enhancement descriptions are moved into the shared enhancement file.

The character page renders its inventory with JavaScript, so its class spans
are not in the initial HTML. The app reads the character ID from the page,
requests AQ's inventory endpoint, and displays the returned class names without
rank suffixes. The interface uses a dark background, red command input, green
Info panel, blue class list, and red errors.

## Test

```bash
.venv/bin/python -m unittest discover -s tests -v
```
