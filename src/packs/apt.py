from src.pack import Pack
from src.utils import print_action, bash


class AptPackages(Pack):
    def __init__(self, packages: list):
        self.packages = packages

    def command_name(self):
        return None

    def depends_on(self):
        return []

    def install(self):
        print_action(f"Installing apt packages: {self.packages}")
        bash(
            f'apt -y install {" ".join(self.packages)}',
            {"DEBIAN_FRONTEND": "noninteractive"},
        )

    def configure(self, configs_dir):
        print_action("Removing unused apt packages")
        bash("apt autoremove -f -y")
