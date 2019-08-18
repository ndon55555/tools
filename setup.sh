#!/usr/bin/env bash

setupDir=""
configDir="$(realpath $(dirname $0))/configurations"
scriptsDir="$(realpath $(dirname $0))/scripts"
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

    action "Running apt-get update"
    apt-get update

    action "Installing curl, wget, python3, and vim are installed"
    apt-get install curl wget python3 vim

    action "Installing zsh and oh-my-zsh"
    apt-get install zsh
    RUNZSH=no sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

    action "Replacing zsh configurations"
    cp -v "$configDir"/.zshrc ~/.zshrc

    action "Replacing vim configurations"
    cp -v "$configDir"/.vimrc ~/.vimrc
    cp -v "$configDir"/.vim/* ~/.vim/

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

    action "Installing Golang 1.12.9"
    wget -O "$setupDir/golang.tar.gz" https://dl.google.com/go/go1.12.9.linux-amd64.tar.gz
    tar -xzf "$setupDir/golang.tar.gz" -C /usr/local/

    action "Installing latest NodeJS"
    pushd "$configDir"
    "$scriptsDir/install-latest-node.sh"
    popd

    action "Installing latest Pip"
    curl https://bootstrap.pypa.io/get-pip.py -o "$setupDir/get-pip.py"
    python3 "$setupDir/get-pip.py"

    action "Installing pynvim" # Makes deoplete plugin for vim work
    pip3 install --user pynvim

    action "Installing vim-plug"
    curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
        https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

    action "Installing vim plugins"
    vim +PlugInstall +qa

    
    if [[ $(ps -p $$ | grep zsh) ]]; then
        action "Running zsh"
        ZSH_DISABLE_COMPFIX=true exec zsh -l
    fi
}

################## Script execution ##################
elevate_privileges
setup
cleanup
