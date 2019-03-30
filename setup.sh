#!/usr/bin/env bash

green='\033[0;31m'
noColor='\033[0m'

action () {
    echo -e "${green}TOOLS SETUP:${noColor} $1..."
}

setupDir="/tmp/setup-tools-tmp"
action "Creating temporary folder for setting up tools"
mkdir "$setupDir"
cd "$setupDir"

action "Installing zsh and oh-my-zsh"
sudo apt install zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
sed -i -e 's/ZSH_THEME="robbyrussell"/ZSH_THEME="af-magic"/' ~/.zshrc # TODO somehow change ZSH_THEME="robbyrussell"
                                                                      # to ZSH_THEME=".*"

action "Adding vim configurations"
cat > ~/.vimrc << VimConfig
" NOTE: Comments in Vim are denoted with a double quote.

set background=dark
set number " Show line numbers
set hlsearch " Highlight search
:highlight lineNr ctermfg=white " Make line numbers white
   
" Tab size = 4
set tabstop=4
set shiftwidth=4
set expandtab
VimConfig

action "Adding tmux configurations"
cat > ~/.tmux.conf <<- TMUXConfig
    set -g mouse on
TMUXConfig

action "Making sure Git and other programs use vim as default editor"
export VISUAL="vim"
export EDITOR="$VISUAL"

action "Installing fuzzy finder"
git clone --depth 1 https://github.com/junegunn/fzf.git
./fzf/install --all

action "Removing temporary folder for setting up tools"
rm -rf setupDir
