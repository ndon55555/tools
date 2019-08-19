#!/usr/bin/env bash

setupDir=""
configDir="$(realpath $(dirname $0))/configurations"
scriptsDir="$(realpath $(dirname $0))/scripts"
user="$(whoami)"
green='\033[0;32m'
noColor='\033[0m'

action () {
    echo -e "${green}TOOLS SETUP:${noColor} $1..."
}

cleanup () {
    action "Removing unused packages"
    sudo apt autoremove -f -y
    action "Removing temporary folder for setting up tools"
    rm -rfv $setupDir
}

setup () {
    setupDir="$(mktemp -d)"
    action "Created temporary folder for setting up tools at $setupDir"

    action "Running apt-get update"
    sudo apt-get -y update

    action "Installing curl, wget, python3, and vim"
    sudo apt-get -y install curl wget python3 vim

    action "Installing zsh and oh-my-zsh"
    sudo apt-get -y install zsh
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
    sudo apt-get -y install silversearcher-ag

    action "Installing Golang 1.12.9"
    wget -O "$setupDir/golang.tar.gz" https://dl.google.com/go/go1.12.9.linux-amd64.tar.gz
    sudo tar -xzf "$setupDir/golang.tar.gz" -C /usr/local/

    action "Installing latest NodeJS"
    pushd "$setupDir"
    sudo "$scriptsDir/install-latest-node.sh"
    popd

    action "Installing python3-distutils" # Need this to get pip
    sudo apt-get install -y python3-distutils
    
    action "Installing latest Pip"
    curl https://bootstrap.pypa.io/get-pip.py -o "$setupDir/get-pip.py"
    sudo python3 "$setupDir/get-pip.py"

    action "Installing pynvim" # Makes deoplete plugin for vim work
    pip3 install --user pynvim

    action "Installing vim-plug"
    curl -fLo "$HOME/.vim/autoload/plug.vim" --create-dirs \
        https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

    action "Installing vim plugins"
    vim +PlugInstall +qa

    action "Ensuring all home files are owned by $user"
    find "$HOME" -maxdepth 1 -name ".*" | xargs -I {} chown -R "$user" {} 

    if [[ -z "$(ps | grep -P "zsh\$")" ]]; then
        action "Running zsh"
        ZSH_DISABLE_COMPFIX=true exec zsh -l
    fi
}

################## Script execution ##################
setup
cleanup
