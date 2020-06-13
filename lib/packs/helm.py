import tempfile
from lib.pack import Pack
from lib.utils import print_action, sh
from os import path


class Helm(Pack):
    def command_name(self):
        return "helm"

    def depends_on(self):
        return []

    def install(self):
        print_action("Installing helm")

        with tempfile.NamedTemporaryFile() as helm_tar_file:
            sh(
                f"wget -O {helm_tar_file.name} https://get.helm.sh/helm-v3.2.1-linux-amd64.tar.gz"
            )

            with tempfile.NamedTemporaryDirectory() as untarred_helm_dir:
                sh(
                    f"tar -xzf {helm_tar_file.name} -C {untarred_helm_dir.name} --strip-components 1"
                )
                sh(
                    f'cp -v {path.join(untarred_helm_dir.name, "helm")} "/usr/local/bin/helm"'
                )

    def configure(self, configs_dir):
        pass
