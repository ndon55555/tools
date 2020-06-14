import requests
import tempfile
from lib.pack import Pack
from lib.utils import print_action, sh


class Node(Pack):
    def command_name(self):
        return "node"

    def depends_on(self):
        return []

    def install(self):
        print_action("Installing latest NodeJS")
        latest_node_version = requests.get(
            "https://resolve-node.now.sh"
        ).content.decode()

        with tempfile.NamedTemporaryFile() as node_tar_file:
            sh(
                f"wget -O {node_tar_file.name} https://nodejs.org/dist/{latest_node_version}/node-{latest_node_version}-linux-x64.tar.gz"
            )
            sh(
                f"tar -xzf {node_tar_file.name} --exclude CHANGELOG.md --exclude LICENSE --exclude README.md --strip-components 1 -C /usr/local"
            )

    def configure(self, configs_dir):
        pass
