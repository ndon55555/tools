import subprocess
from os import environ, path
from typing import Dict, Optional

from colorama import Fore

home_dir = path.expanduser("~")


def bash(cmd: str, env: Optional[Dict[str, str]] = None, suppress_output: bool = False):
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

    r = subprocess.run(
        cmd,
        env=effective_env,
        check=True,
        shell=True,
        executable="/usr/bin/bash",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )

    print(r.stdout.decode("utf-8"))
    return r.stdout.decode("utf-8")


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

    symlink(path.join(src_dir, config), path.join(dst_dir, config))


def symlink(src: str, dst: str):
    bash(f"mkdir -p {path.dirname(dst)}")
    bash(f"ln -fns {src} {dst}")