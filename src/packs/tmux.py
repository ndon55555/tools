from src.pack import Pack
from src.packs.apt import AptPackages
from src.utils import home_dir, symlink_config, print_action


class Tmux(Pack):
    def command_name(self):
        return "tmux"

    def depends_on(self):
        return [AptPackages(["tmux"])]

    def install(self):
        pass

    def configure(self, configs_dir):
        print_action("Symlinking tmux configurations")
        symlink_config(configs_dir, home_dir, ".tmux.conf")
