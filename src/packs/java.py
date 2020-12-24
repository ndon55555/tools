import tempfile
from src.pack import Pack
from src.utils import print_action, sh


class Java(Pack):
    def command_name(self):
        return "java"

    def depends_on(self):
        return []

    def install(self):
        print_action("Installing Java 13.0.2")

        with tempfile.NamedTemporaryFile() as java_tar_file:
            sh(
                f"wget -O {java_tar_file.name} https://github.com/AdoptOpenJDK/openjdk13-binaries/releases/download/jdk-13.0.2+8/OpenJDK13U-jdk_x64_linux_hotspot_13.0.2_8.tar.gz"
            )
            sh("mkdir -p /usr/local/jdk")
            sh(f"tar -xzf {java_tar_file.name} -C /usr/local/jdk --strip-components 1")

    def configure(self, configs_dir):
        pass
