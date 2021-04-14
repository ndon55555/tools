import os.path as path
import subprocess
from src.pack import Pack
from src.utils import bash


def command_available(cmd: str):
    try:
        bash(f"command -v {cmd}", suppress_output=True)
        return True
    except subprocess.CalledProcessError:
        return False


def cached_install(pack: Pack):
    cmd = pack.command_name()

    if cmd is None or not command_available(cmd):
        for dep in pack.depends_on():
            cached_install(dep)

        pack.install()
        pack.configure(
            path.join(path.dirname(path.abspath(__file__)), "configurations")
        )


def setup():
    from src.packs.ag import Ag
    from src.packs.asdf import Asdf
    from src.packs.docker import Docker
    from src.packs.fzf import Fzf
    from src.packs.git import Git
    from src.packs.go import Go
    from src.packs.helm import Helm
    from src.packs.java import Java
    from src.packs.k3d import K3d
    from src.packs.kubectl import Kubectl
    from src.packs.node import Node
    from src.packs.npm import Npm
    from src.packs.tmux import Tmux
    from src.packs.vim import Vim
    from src.packs.zsh import Zsh

    packs = [
        Ag(),
        Asdf(),
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
