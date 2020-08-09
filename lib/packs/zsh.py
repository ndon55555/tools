from lib.pack import Pack
from lib.packs.apt import AptPackages
from lib.utils import home_dir, print_action, sh, symlink_config


class Zsh(Pack):
    def command_name(self):
        return "zsh"

    def depends_on(self):
        return [AptPackages(["zsh"])]

    def install(self):
        print_action("Installing oh-my-zsh")
        sh(
            env={"RUNZSH": "no"},
            cmd='sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)" || true',
        )

    def configure(self, configs_dir):
        print_action("Symlinking zsh configurations")
        symlink_config(configs_dir, home_dir, ".zshrc")