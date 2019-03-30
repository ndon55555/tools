#!/usr/bin/env bash

setupDir="/tmp/setup-tmp"
mkdir "$setupDir"
cd "$setupDir"

# Install zsh and oh-my-zsh
sudo apt install zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
sed -i -e 's/ZSH_THEME="robbyrussell"/ZSH_THEME="af-magic"/' ~/.zshrc # TODO somehow change ZSH_THEME="robbyrussell"
                                                                      # to ZSH_THEME=".*"

# Add vim configurations
cat >> ~/.vimrc <<- VimConfig
    set background=dark
    set number # Show line numbers
    set hlsearch # Highlight search
    :highlight lineNr ctermfg=white # Make line numbers white
    
    # Tab size = 4
    set tabstop=4
    set shiftwidth=4
    set expandtab
VimConfig

# Add tmux configurations
cat >> ~/.tmux.conf <<- TMUXConfig
    set -g mouse on
TMUXConfig

# Make sure Git and other programs use vim as default editor
export VISUAL="vim"
export EDITOR="$VISUAL"
