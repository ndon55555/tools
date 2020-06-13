#!/usr/bin/env bash

# Elevate to sudo and run commands as current user
if [[ "$EUID" != 0 ]]; then 
    sudo --preserve-env PATH="$PATH" env "$0" "$@" --user="$(whoami)" --set-home
    exit $?
fi

user="$SUDO_USER"
tools_dir="$(realpath $(dirname $0))"
green='\033[0;32m'
noColor='\033[0m'

action () {
    echo -e "${green}TOOLS SETUP:${noColor} $1"
}

setup () {
    action "Running apt-get update"
    apt-get -y update

    action "Installing python3"
    apt-get -y install python3

    action "Installing latest Pip"
    apt-get -y install python3-venv python3-pip

    action "Installing poetry"
    pip install --user poetry

    poetry run python3 "$tools_dir/install.py" "$user"
}

################## Script execution ##################
setup
