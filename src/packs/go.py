import tempfile
from src.pack import Pack
from src.utils import print_action, sh


class Go(Pack):
    def command_name(self):
        return "go"

    def depends_on(self):
        return []

    def install(self):
        print_action("Installing Golang 1.13.8")

        with tempfile.NamedTemporaryFile() as golang_tar_file:
            sh(
                f"wget -O {golang_tar_file.name} https://dl.google.com/go/go1.13.8.linux-amd64.tar.gz"
            )
            sh(f"tar -xzf {golang_tar_file.name} -C /usr/local/")

    def configure(self, configs_dir):
        pass
