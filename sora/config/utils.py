import os
from pathlib import Path


def get_config_path():
    """
    Gets the path to the config directory.
    """

    user_config = Path(os.getenv("XDG_CONFIG_HOME", "~/.config")).expanduser()
    return user_config.joinpath("sora")
