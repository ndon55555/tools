from lib.pack import Pack
from lib.packs.docker import Docker
from lib.utils import print_action, sh


class K3d(Pack):
    def command_name(self):
        return "k3d"

    def depends_on(self):
        return [Docker()]

    def install(self):
        print_action("Installing k3d")
        sh(
            "wget -q -O - https://raw.githubusercontent.com/rancher/k3d/master/install.sh | bash"
        )

    def configure(self, configs_dir):
        pass
