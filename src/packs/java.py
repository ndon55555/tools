from src.pack import Pack
from src.packs.asdf import Asdf
from src.utils import print_action


class Java(Pack):
    def __init__(self):
        self._asdf = Asdf()

    def command_name(self):
        return "java"

    def depends_on(self):
        return []

    def install(self):
        print_action("Installing Java")

        self._asdf.bash_with_asdf_available(
            "asdf plugin-add java https://github.com/halcyon/asdf-java.git || true"
        )
        self._asdf.bash_with_asdf_available("asdf install java latest:adoptopenjdk-11")
        self._asdf.bash_with_asdf_available(
            f"asdf global java {self._asdf.latest_installed_version('java adoptopenjdk-11')}"
        )

    def configure(self, configs_dir):
        pass
