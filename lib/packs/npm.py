from lib.pack import Pack
from lib.packs.node import Node
from lib.utils import home_dir, print_action, sh
from os import path


class Npm(Pack):
    def command_name(self):
        return "npm"

    def depends_on(self):
        return [Node()]

    def install(self):
        pass

    def configure(self, configs_dir):
        print_action("Configuring NPM")
        npm_packages_dir = path.join(home_dir, ".npm-packages")
        sh(f"mkdir -p {npm_packages_dir}")
        sh(f"npm config set prefix {npm_packages_dir}")
