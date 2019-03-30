#!/usr/bin/env bash

setupDir="/tmp/setup-tools-tmp"
green='\033[0;32m'
noColor='\033[0m'

action () {
    echo -e "${green}TOOLS SETUP:${noColor} $1..."
}

elevate_privileges () {
    if [ $EUID != 0 ]; then
        sudo "$0" "$@"
        exit $?
    fi
}

cleanup () {
    action "Removing unused packages"
    apt autoremove -f
    action "Removing temporary folder for setting up tools"
    rm -rfv $setupDir
}

setup () {
    action "Creating temporary folder for setting up tools at $setupDir"
    mkdir "$setupDir"

    action "Installing zsh and oh-my-zsh"
    apt install zsh
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

    action "Replacing vim configurations"
    cp "$(dirname $0)"/configurations/.vimrc ~/.vimrc

    action "Replacing tmux configurations"
    cp "$(dirname $0)"/configurations/.tmux.conf ~/.tmux.conf

    action "Making sure Git and other programs use vim as default editor"
    export VISUAL="vim"
    export EDITOR="$VISUAL"

    action "Installing fuzzy finder"
    git clone --depth 1 https://github.com/junegunn/fzf.git "$setupDir"/fzf
    pushd ~
        "${setupDir}"/fzf/install --all
    popd
}

################## Script execution ##################
elevate_privileges
setup
cleanup
