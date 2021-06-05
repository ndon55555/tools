from src.pack import Pack
from src.packs.apt import AptPackages
from src.utils import bash, home_dir, print_action, symlink, symlink_config


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

        print_action("Setting up typewritten")
        bash(
            "git clone https://github.com/reobin/typewritten.git $ZSH_CUSTOM/themes/typewritten || true"
        )
        symlink("$ZSH_CUSTOM/themes/typewritten/typewritten.zsh-theme", "$ZSH_CUSTOM/themes/typewritten.zsh-theme")
        symlink("$ZSH_CUSTOM/themes/typewritten/async.zsh", "$ZSH_CUSTOM/themes/async")
