#!/usr/bin/env bash
set -euo pipefail

PROJECT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$PROJECT_DIR/.venv"
VENV_PYTHON="$VENV_DIR/bin/python"
LAUNCHER="$VENV_DIR/bin/aqwhelper"
BIN_DIR="${HOME:?HOME must be set}/.local/bin"
COMMAND_PATH="$BIN_DIR/aqwhelper"

confirm() {
    local answer
    while true; do
        printf '%s [y/n] ' "$1" >&2
        read -r answer || answer=""
        case "${answer}" in
            y|yes) return 0 ;;
            ""|n|no) return 1 ;;
            *) printf 'Please answer yes or no.\n' ;;
        esac
    done
}

add_bash_path() {
    local config_file="$1"
    local marker="# Added by AQW Helper installer"

    if [[ -f "$config_file" ]] && grep -Fq "$marker" "$config_file"; then
        printf 'Bash PATH setup already exists in %s.\n' "$config_file"
        return
    fi
    if [[ -f "$config_file" ]] && grep -Fq '.local/bin' "$config_file"; then
        printf '~/.local/bin already appears to be configured in %s; leaving it unchanged.\n' \
            "$config_file"
        return
    fi

    {
        printf '\n%s\n' "$marker"
        printf 'export PATH="$HOME/.local/bin:$PATH"\n'
    } >> "$config_file"
    printf 'Configured Bash PATH in %s.\n' "$config_file"
}

printf 'AQW Helper setup\n'
printf 'This installs the terminal app; it does not open a separate desktop window.\n\n'

if ! command -v python3 >/dev/null 2>&1; then
    printf 'Error: python3 is required. Install Python 3 and run this installer again.\n' >&2
    exit 1
fi

if [[ ! -x "$VENV_PYTHON" ]]; then
    if ! confirm "Create a Python virtual environment at $VENV_DIR?"; then
        printf 'Setup stopped: the app needs this virtual environment.\n'
        exit 0
    fi
    if ! python3 -m venv "$VENV_DIR"; then
        printf 'Error: could not create the virtual environment.\n' >&2
        printf 'On Debian/Ubuntu, install it with: sudo apt install python3-venv\n' >&2
        exit 1
    fi
else
    printf 'Using existing virtual environment: %s\n' "$VENV_DIR"
fi

if confirm "Install or update AQW Helper and its Python dependencies in this environment?"; then
    "$VENV_PYTHON" -m pip install --editable "$PROJECT_DIR"
elif [[ ! -x "$LAUNCHER" ]]; then
    printf 'App installation skipped.\n'
else
    printf 'AQW Helper is already installed in the virtual environment.\n'
fi

if [[ ! -x "$LAUNCHER" ]]; then
    printf '\nThe app is not installed, so a global aqwhelper command cannot be created.\n'
    printf 'Run this installer again and approve app installation to continue.\n'
    exit 0
fi

if [[ -e "$COMMAND_PATH" || -L "$COMMAND_PATH" ]]; then
    if [[ ! -L "$COMMAND_PATH" || "$(readlink -- "$COMMAND_PATH")" != "$LAUNCHER" ]]; then
        printf 'Error: %s already exists and is not this project launcher; leaving it unchanged.\n' \
            "$COMMAND_PATH" >&2
        exit 1
    fi
    printf 'The aqwhelper command is already installed at %s.\n' "$COMMAND_PATH"
else
    if confirm "Add the aqwhelper command at $COMMAND_PATH?"; then
        mkdir -p "$BIN_DIR"
        ln -s "$LAUNCHER" "$COMMAND_PATH"
        printf 'Installed command: %s\n' "$COMMAND_PATH"
    else
        printf 'Command registration skipped. You can run %s directly.\n' "$LAUNCHER"
        exit 0
    fi
fi

if confirm "Add ~/.local/bin to Bash PATH in ~/.profile and ~/.bashrc?"; then
    mkdir -p "$HOME"
    touch "$HOME/.profile" "$HOME/.bashrc"
    add_bash_path "$HOME/.profile"
    add_bash_path "$HOME/.bashrc"
else
    printf 'Bash PATH setup skipped.\n'
fi

FISH_CONFIG_DIR="$HOME/.config/fish/conf.d"
FISH_CONFIG="$FISH_CONFIG_DIR/aqw-helper.fish"
if [[ -f "$FISH_CONFIG" ]] && grep -Fq 'fish_add_path "$HOME/.local/bin"' "$FISH_CONFIG"; then
    printf 'Fish PATH setup already exists in %s.\n' "$FISH_CONFIG"
elif confirm "Add ~/.local/bin to Fish PATH?"; then
    mkdir -p "$FISH_CONFIG_DIR"
    printf '\n# Added by AQW Helper installer\nfish_add_path "$HOME/.local/bin"\n' >> "$FISH_CONFIG"
    printf 'Configured Fish PATH in %s.\n' "$FISH_CONFIG"
else
    printf 'Fish PATH setup skipped.\n'
fi

printf '\nSetup complete. Open a new terminal to run aqwhelper from any directory.\n'
if confirm "Start AQW Helper in this terminal now?"; then
    exec "$COMMAND_PATH"
fi
printf 'You can start it later by running: aqwhelper\n'
