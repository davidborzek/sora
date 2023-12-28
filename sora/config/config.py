import sys
from pathlib import Path
import importlib

from sora.window import Window


class ConfigError(Exception):
    """
    Raised when there is an error in the config file.
    """

    pass


class Config:
    """
    Represents the widget configuration.
    """

    windows: list[Window]

    def __init__(self, path: Path):
        """
        Creates a new config for the given path.

        :param path: The path to the config file.
        """

        self.path = path.joinpath("config.py")
        self.load()

    def load(self):
        """
        Loads the config python module.
        """

        if not self.path.exists():
            raise ConfigError(f"{self.path} does not exists")

        name = self.path.stem

        sys.path.insert(0, self.path.parent.as_posix())

        # TODO: implement reloading
        config = importlib.import_module(name)

        for key in self.__annotations__.keys():
            try:
                value = vars(config)[key]
                setattr(self, key, value)
            except KeyError:
                if getattr(self, key, None) is None:
                    raise ConfigError(f"Required key '{key}' not set.")
