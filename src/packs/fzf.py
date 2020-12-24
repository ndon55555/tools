from src.pack import Pack
from src.packs.git import Git
from src.utils import home_dir, print_action, sh
from os import path


class Fzf(Pack):
    def command_name(self):
        return "fzf"

    def depends_on(self):
        return [Git()]

    def install(self):
        print_action("Installing fuzzy finder")
        # The repo is downloaded to HOME because it contains binaries that make the tool work
        fzf_dir = path.join(home_dir, ".fzf")
        sh(f"git clone --depth 1 https://github.com/junegunn/fzf.git {fzf_dir} || true")
        sh(f"{fzf_dir}/install --all")

    def configure(self, configs_dir):
        pass
