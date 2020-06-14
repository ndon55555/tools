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

    action "Installing sudo"
    apt-get -y install sudo

    action "Installing curl and wget"
    apt-get -y install curl wget

    action "Installing python3"
    apt-get -y install python3

    action "Installing pip3"
    apt-get -y install python3-venv python3-pip
    pip3 install --upgrade pip
    pip3 install --upgrade keyrings.alt # Somehow resolves a problem seen after upgrading pip

    action "Installing poetry"
    pip3 install --user poetry

    LANG="C.UTF-8" PATH="$PATH:$HOME/.local/bin" poetry install
    LANG="C.UTF-8" PATH="$PATH:$HOME/.local/bin" poetry run python3 "$tools_dir/install.py"
}

################## Script execution ##################
pushd "$tools_dir"
    setup
popd
