from src.pack import Pack
from src.packs.asdf import Asdf
from src.utils import print_action


class Node(Pack):
    def __init__(self):
        self._asdf = Asdf()

    def command_name(self):
        return "node"

    def depends_on(self):
        return []

    def install(self):
        print_action("Installing NodeJS")
        self._asdf.bash_with_asdf_available("asdf plugin-add nodejs || true")
        self._asdf.bash_with_asdf_available("asdf install nodejs latest")
        self._asdf.bash_with_asdf_available(
            f"asdf global nodejs {self._asdf.latest_installed_version('nodejs')}"
        )

    def configure(self, configs_dir):
        pass
