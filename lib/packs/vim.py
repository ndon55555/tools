from lib.pack import Pack
from lib.packs.apt import AptPackages
from lib.utils import home_dir, print_action, sh, symlink_config
from os import path


class Vim(Pack):
    def command_name(self):
        return "vim"

    def depends_on(self):
        return [AptPackages("zsh")]

    def install(self):
        print_action("Installing oh-my-zsh")
        sh(
            env={"RUNZSH": "no"},
            cmd='sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)" || true',
        )

    def configure(self, configs_dir):
        print_action("Symlinking vim configurations")
        symlink_config(configs_dir, home_dir, ".vimrc")
        symlink_config(configs_dir, home_dir, path.join(".vim", "coc-settings.json"))

        print_action("Installing pynvim")  # Makes deoplete plugin for vim work
        sh("pip3 install --user pynvim")

        print_action("Installing vim-plug")
        vim_plug_file = path.join(home_dir, ".vim", "autoload", "plug.vim")
        sh(
            f"curl -fLo {vim_plug_file} --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim"
        )

        print_action("Installing vim plugins")
        sh("vim +PlugInstall +qa")
