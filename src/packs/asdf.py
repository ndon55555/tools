from src.pack import Pack
from src.packs.git import Git
from src.utils import bash, print_action, home_dir

ASDF_DIR = f"{home_dir}/.asdf"


class Asdf(Pack):
    def command_name(self):
        "asdf"

    def depends_on(self):
        return [Git()]

    def install(self):
        print_action("Installing asdf")
        bash(f"git clone https://github.com/asdf-vm/asdf.git {ASDF_DIR} || true")
        bash(
            f'pushd {ASDF_DIR} && git checkout "$(git describe --abbrev=0 --tags)" && popd'
        )
        bash(f"source {ASDF_DIR}/asdf.sh")

    def configure(self, configs_dir: str):
        pass

    def bash_with_asdf_available(self, cmd, env=None):
        return bash(f"source {ASDF_DIR}/asdf.sh && {cmd}", env)

    def latest_installed_version(self, plugin_name):
        r = self.bash_with_asdf_available(f"asdf latest {plugin_name}")

        if len(r) == 0:
            return None

        return r
