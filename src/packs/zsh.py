from src.pack import Pack
from src.packs.apt import AptPackages
from src.utils import home_dir, print_action, bash, symlink_config


class Zsh(Pack):
    def command_name(self):
        return "zsh"

    def depends_on(self):
        return [AptPackages(["zsh"])]

    def install(self):
        print_action("Installing oh-my-zsh")
        bash(
            'sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)" || true',
            {"CHSH": "no", "RUNZSH": "no"},
        )

    def configure(self, configs_dir):
        print_action("Symlinking zsh configurations")
        symlink_config(configs_dir, home_dir, ".zshrc")
