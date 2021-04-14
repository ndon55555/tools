from src.pack import Pack
from src.packs.asdf import Asdf
from src.packs.docker import Docker
from src.utils import print_action


class K3d(Pack):
    def __init__(self):
        self._asdf = Asdf()

    def command_name(self):
        return "k3d"

    def depends_on(self):
        return [Docker()]

    def install(self):
        print_action("Installing k3d")
        self._asdf.bash_with_asdf_available(
            "asdf plugin-add k3d https://github.com/spencergilbert/asdf-k3d.git || true"
        )
        self._asdf.bash_with_asdf_available("asdf install k3d latest")
        self._asdf.bash_with_asdf_available(
            f"asdf global k3d {self._asdf.latest_installed_version('k3d')}"
        )

    def configure(self, configs_dir):
        pass
