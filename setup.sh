#!/usr/bin/env bash

setupDir="/tmp/setup-tools-tmp"
configDir="$(dirname $0)/configurations"
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

    action "Replacing zsh configurations"
    cp -v "$configDir"/.zshrc ~/.zshrc

    action "Replacing vim configurations"
    cp -v "$configDir"/.vimrc ~/.vimrc

    action "Replacing tmux configurations"
    cp -v "$configDir"/.tmux.conf ~/.tmux.conf

    action "Replacing git configurations"
    cp -v "$configDir"/.gitconfig ~/.gitconfig

    action "Installing fuzzy finder"
    git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
    pushd ~
        .fzf/install --all
    popd
}

################## Script execution ##################
elevate_privileges
setup
cleanup
