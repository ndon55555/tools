from src.pack import Pack
from src.packs.asdf import Asdf
from src.utils import print_action


class Helm(Pack):
    def __init__(self):
        self._asdf = Asdf()

    def command_name(self):
        return "helm"

    def depends_on(self):
        return []

    def install(self):
        print_action("Installing helm")
        self._asdf.bash_with_asdf_available(
            "asdf plugin-add helm https://github.com/Antiarchitect/asdf-helm.git || true"
        )
        self._asdf.bash_with_asdf_available("asdf install helm latest")
        self._asdf.bash_with_asdf_available(
            f"asdf global helm {self._asdf.latest_installed_version('helm')}"
        )

    def configure(self, configs_dir):
        pass
