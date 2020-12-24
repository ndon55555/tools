import subprocess
from colorama import Fore
from os import environ, path
from typing import Dict, Optional

home_dir = path.expanduser("~")


def sh(cmd: str, env: Optional[Dict[str, str]] = None, suppress_output: bool = False):
    # TODO suppress_output
    """
    Runs a shell command. Raises an error/exception if the command fails.

    Args:
        cmd: The command to run.
        env: The environment variables to patch the current environment with.
    """
    effective_env = environ.copy()
    if env is not None:
        effective_env.update(env)

    subprocess.run(
        cmd, env=effective_env, check=True, shell=True,
    )


def print_action(action: str):
    """
    Stylizes and prints the given action to standard out.

    Args:
        action: The action being performed by this script.
    """
    print(f"{Fore.GREEN}TOOLS SETUP:{Fore.RESET} {action}")


def symlink_config(src_dir: str, dst_dir: str, config: str):
    if path.isabs(config):
        raise ValueError("config path must be relative to src_dir")

    dst_dir = path.join(dst_dir, path.dirname(config))
    sh(f"mkdir -p {dst_dir}")
    sh(
        "ln -fs {src} {dst}".format(
            src=path.join(src_dir, config),
            dst=path.join(dst_dir, path.basename(config)),
        )
    )
