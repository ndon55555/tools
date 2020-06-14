import os.path as path
import subprocess
from lib.pack import Pack
from lib.utils import sh


def command_available(cmd: str):
    try:
        sh(f"command -v {cmd}", suppress_output=True)
        return True
    except subprocess.CalledProcessError:
        return False


def cached_install(pack: Pack):
    cmd = pack.command_name()

    if cmd is None or not command_available(cmd):
        for dep in pack.depends_on():
            cached_install(dep)

        pack.install()

    pack.configure(path.join(path.dirname(path.abspath(__file__)), "configurations"))


def setup():
    from lib.packs.ag import Ag
    from lib.packs.docker import Docker
    from lib.packs.fzf import Fzf
    from lib.packs.git import Git
    from lib.packs.go import Go
    from lib.packs.helm import Helm
    from lib.packs.java import Java
    from lib.packs.k3d import K3d
    from lib.packs.kubectl import Kubectl
    from lib.packs.node import Node
    from lib.packs.npm import Npm
    from lib.packs.tmux import Tmux
    from lib.packs.vim import Vim
    from lib.packs.zsh import Zsh

    packs = [
        Ag(),
        Docker(),
        Fzf(),
        Git(),
        Go(),
        Helm(),
        Java(),
        K3d(),
        Kubectl(),
        Node(),
        Npm(),
        Tmux(),
        Vim(),
        Zsh(),
    ]

    for pack in packs:
        cached_install(pack)


def main():
    setup()


main()
