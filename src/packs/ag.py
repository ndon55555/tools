from src.pack import Pack
from src.packs.apt import AptPackages


class Ag(Pack):
    def command_name(self):
        return "ag"

    def depends_on(self):
        return [AptPackages(["silversearcher-ag"])]

    def install(self):
        pass

    def configure(self, configs_dir):
        pass
