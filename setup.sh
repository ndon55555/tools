#!/usr/bin/env bash

setupDir=""
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
    apt autoremove -f -y
    action "Removing temporary folder for setting up tools"
    rm -rfv $setupDir
}

setup () {
    setupDir="$(mktemp -d)"
    action "Created temporary folder for setting up tools at $setupDir"

    action "Installing zsh and oh-my-zsh"
    apt-get install zsh
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

    action "Installing The Silver Searcher"
    apt-get install silversearcher-ag

    action "Installing Golang"
    wget -O "$setupDir/golang.tar.gz" https://dl.google.com/go/go1.12.9.linux-amd64.tar.gz
    tar -xzf "$setupDir/golang.tar.gz" -C /usr/local/

    action "Sourcing .zshrc"
    source ~/.zshrc
}

################## Script execution ##################
elevate_privileges
setup
cleanup
