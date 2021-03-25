from src.pack import Pack
from src.packs.node import Node
from src.utils import home_dir, print_action, sh
from os import path


class Npm(Pack):
    def command_name(self):
        return "npm"

    def depends_on(self):
        return [Node()]

    def install(self):
        pass

    def configure(self, configs_dir):
        pass
