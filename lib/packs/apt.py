from lib.pack import Pack
from lib.utils import print_action, sh


class AptPackages(Pack):
    def __init__(self, packages: list):
        self.packages = packages

    def command_name(self):
        return None

    def depends_on(self):
        return []

    def install(self):
        print_action(f"Installing apt packages: {self.packages}")
        sh(f'apt-get -y install {" ".join(self.packages)}')

    def configure(self, configs_dir):
        print_action("Removing unused apt packages")
        sh("apt autoremove -f -y")
