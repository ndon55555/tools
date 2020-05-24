#!/usr/bin/env bash

# Elevate to sudo and run commands as current user
if [[ "$EUID" != 0 ]]; then
    sudo "$0" "$@" --user="$(whoami)" --set-home
    exit $?
fi

user="$SUDO_USER"
setupDir=""
configDir="$(realpath $(dirname $0))/configurations"
scriptsDir="$(realpath $(dirname $0))/scripts"
green='\033[0;32m'
noColor='\033[0m'

action () {
    echo -e "${green}TOOLS SETUP:${noColor} $1..."
}

cachedInstall () {
    tool=$1
}

cleanup () {
    action "Removing unused packages"
    apt autoremove -f -y
    action "Removing temporary folder for setting up tools"
    rm -rfv "$setupDir"
}

setup () {
    setupDir="$(mktemp -d)"
    action "Created temporary folder for setting up tools at $setupDir"

    action "Running apt-get update"
    apt-get -y update

    action "Installing curl, wget, python3, and vim"
    apt-get -y install curl wget python3 vim

    action "Installing zsh and oh-my-zsh"
    apt-get -y install zsh
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
    cp -v "$configDir"/.gitignore-global ~/.gitignore-global
    git config --global core.excludesfile ~/.gitignore-global

    action "Installing fuzzy finder"
    git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
    pushd ~
    .fzf/install --all
    popd

    action "Installing The Silver Searcher"
    apt-get -y install silversearcher-ag

    action "Installing Golang 1.13.8"
    wget -O "$setupDir/golang.tar.gz" https://dl.google.com/go/go1.13.8.linux-amd64.tar.gz
    tar -xzf "$setupDir/golang.tar.gz" -C /usr/local/

    action "Installing latest NodeJS"
    pushd "$setupDir"
    "$scriptsDir/install-latest-node.sh"
    popd

    action "Configuring NPM"
    mkdir "$HOME/.npm-packages"
    npm config set prefix "$HOME/.npm-packages"

    action "Installing Java 13.0.2"
    wget -O "$setupDir/jdk.tar.gz" https://github.com/AdoptOpenJDK/openjdk13-binaries/releases/download/jdk-13.0.2+8/OpenJDK13U-jdk_x64_linux_hotspot_13.0.2_8.tar.gz
    mkdir -p /usr/local/jdk
    tar -xzf "$setupDir/jdk.tar.gz" -C /usr/local/jdk --strip-components 1

    action "Installing python3-distutils" # Need this to get pip
    apt-get install -y python3-distutils

    action "Installing latest Pip"
    curl https://bootstrap.pypa.io/get-pip.py -o "$setupDir/get-pip.py"
    python3 "$setupDir/get-pip.py"

    action "Installing pynvim" # Makes deoplete plugin for vim work
    pip3 install --user pynvim

    action "Installing vim-plug"
    curl -fLo "$HOME/.vim/autoload/plug.vim" --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

    action "Installing vim plugins"
    vim +PlugInstall +qa

    action "Ensuring all home files are owned by $user"
    find "$HOME" -maxdepth 1 -name ".*" | xargs -I {} chown -R "$user:$user" {}

    if [[ ! -x "$(command -v docker)" ]]; then
        action "docker not present. Installing docker"
        # Ensure clean installation
        apt-get -y remove docker docker-engine docker.io containerd runc
        apt-get -y install apt-transport-https ca-certificates gnupg-agent software-properties-common
        curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
        add-apt-repository -y "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
        apt-get -y update
        apt-get install docker-ce docker-ce-cli containerd.io
    fi

    if [[ ! -x "$(command -v k3d)" ]]; then
        action "k3d not present. Installing k3d"
        wget -q -O - https://raw.githubusercontent.com/rancher/k3d/master/install.sh | bash
    fi

    if [[ ! -x "$(command -v kubectl)" ]]; then
        action "kubectl not present. Installing kubectl"
        curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl
    fi

    if [[ ! -x "$(command -v helm)" ]]; then
        action "helm not present. Installing helm"
        wget -O "$setupDir/helm.tar.gz" https://get.helm.sh/helm-v3.2.1-linux-amd64.tar.gz
        mkdir "$setupDir/helm-contents"
        tar -xzf "$setupDir/helm.tar.gz" -C "$setupDir/helm-contents" --strip-components 1
        cp -v "$setupDir/helm-contents/helm" "/usr/local/bin/helm"
    fi
}

################## Script execution ##################
setup
cleanup
