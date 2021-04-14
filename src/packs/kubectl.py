from src.pack import Pack
from src.packs.asdf import Asdf
from src.utils import print_action


class Kubectl(Pack):
    def __init__(self):
        self._asdf = Asdf()

    def command_name(self):
        return "kubectl"

    def depends_on(self):
        return []

    def install(self):
        print_action("Installing kubectl")
        self._asdf.bash_with_asdf_available(
            "asdf plugin-add kubectl https://github.com/Banno/asdf-kubectl.git || true"
        )
        self._asdf.bash_with_asdf_available("asdf install kubectl latest")
        self._asdf.bash_with_asdf_available(
            f"asdf global kubectl {self._asdf.latest_installed_version('kubectl')}"
        )

    def configure(self, configs_dir):
        pass
