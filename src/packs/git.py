from src.pack import Pack
from src.packs.apt import AptPackages
from src.utils import home_dir, print_action, sh, symlink_config
from os import path


class Git(Pack):
    def command_name(self):
        return "git"

    def depends_on(self):
        return [AptPackages(["git"])]

    def install(self):
        pass

    def configure(self, configs_dir):
        print_action("Symlinking git configurations")
        symlink_config(configs_dir, home_dir, ".gitconfig")
        symlink_config(configs_dir, home_dir, ".gitignore-global")
        print_action("Setting global gitignore file")
        sh(
            "git config --global core.excludesfile {}".format(
                path.join(home_dir, ".gitignore-global")
            )
        )
