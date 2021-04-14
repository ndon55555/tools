from src.pack import Pack
from src.packs.apt import AptPackages
from src.utils import home_dir, print_action, bash, symlink_config
from os import path


class Vim(Pack):
    def command_name(self):
        return "vim"

    def depends_on(self):
        return [AptPackages(["vim"])]

    def install(self):
        pass

    def configure(self, configs_dir):
        print_action("Symlinking vim configurations")
        symlink_config(configs_dir, home_dir, ".vimrc")
        symlink_config(configs_dir, home_dir, path.join(".vim", "coc-settings.json"))

        bash(
            "/usr/local/bin/pip3 install --user pynvim"
        )  # Make sure to use system pip3, not the one in the virtual environment

        print_action("Installing vim-plug")
        vim_plug_file = path.join(home_dir, ".vim", "autoload", "plug.vim")
        bash(
            f"curl -fLo {vim_plug_file} --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim"
        )

        print_action("Installing vim plugins")
        bash("vim +PlugInstall +GoInstallBinaries +qa")
