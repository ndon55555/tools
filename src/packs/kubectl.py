from src.pack import Pack
from src.utils import print_action, sh


class Kubectl(Pack):
    def command_name(self):
        return "kubectl"

    def depends_on(self):
        return []

    def install(self):
        print_action("Installing kubectl")
        sh(
            "wget -O /usr/local/bin/kubectl https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl"
        )

    def configure(self, configs_dir):
        sh("chmod +x /usr/local/bin/kubectl")
