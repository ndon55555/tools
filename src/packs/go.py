from src.pack import Pack
from src.packs.asdf import Asdf
from src.utils import print_action


class Go(Pack):
    def __init__(self):
        self._asdf = Asdf()

    def command_name(self):
        return "go"

    def depends_on(self):
        return []

    def install(self):
        print_action("Installing Golang")
        self._asdf.bash_with_asdf_available(
            "asdf plugin-add golang https://github.com/kennyp/asdf-golang.git || true"
        )
        self._asdf.bash_with_asdf_available("asdf install golang latest")
        self._asdf.bash_with_asdf_available(
            f"asdf global golang {self._asdf.latest_installed_version('golang')}"
        )

    def configure(self, configs_dir):
        pass
