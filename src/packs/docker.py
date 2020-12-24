from src.pack import Pack
from src.packs.apt import AptPackages
from src.utils import print_action, sh


class Docker(Pack):
    def command_name(self):
        return "docker"

    def depends_on(self):
        return [
            AptPackages(
                [
                    "apt-transport-https",
                    "ca-certificates",
                    "gnupg-agent",
                    "software-properties-common",
                ]
            )
        ]

    def install(self):
        print_action("Installing docker")
        # Ensure clean installation
        sh("apt-get -y remove docker docker-engine docker.io containerd runc")
        sh(
            "apt-get -y install apt-transport-https ca-certificates gnupg-agent software-properties-common"
        )
        sh(
            "curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -"
        )
        sh(
            'add-apt-repository -y "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"'
        )
        sh("apt-get -y update")
        AptPackages(
            ["docker-ce", "docker-ce-cli", "docker-ce-cli", "containerd.io"]
        ).install()

    def configure(self, configs_dir):
        print_action("Starting docker service")
        sh("sudo service docker start || true")
