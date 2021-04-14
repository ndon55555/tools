from os import path

from src.pack import Pack
from src.packs.asdf import Asdf
from src.utils import print_action


class Fzf(Pack):
    def __init__(self):
        self._asdf = Asdf()

    def command_name(self):
        return "fzf"

    def depends_on(self):
        return [self._asdf]

    def install(self):
        print_action("Installing fuzzy finder")
        self._asdf.bash_with_asdf_available(
            "asdf plugin add fzf https://github.com/kompiro/asdf-fzf.git || true"
        )
        self._asdf.bash_with_asdf_available("asdf install fzf latest")
        self._asdf.bash_with_asdf_available(
            f"asdf global fzf {self._asdf.latest_installed_version('fzf')}"
        )
        self._asdf.bash_with_asdf_available("$(asdf where fzf)/install --all")

    def configure(self, configs_dir):
        pass
