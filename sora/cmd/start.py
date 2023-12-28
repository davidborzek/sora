from pathlib import Path
import gi

from argparse import Namespace, BooleanOptionalAction
import logging
import os

from sora.config.utils import get_config_path


def run(options: Namespace):
    if options.inspector:
        os.environ["GTK_DEBUG"] = "interactive"

    # This must be happen first.
    gi.require_version("Gtk", "3.0")

    from sora.app import App
    from sora.config.config import Config

    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)

    config_path = Path(options.config)
    config = Config(config_path)

    try:
        app = App(config)

        app.run()
    except KeyboardInterrupt:
        pass


def subcommand(subparsers):
    cmd = subparsers.add_parser("start", help="Start sora.")
    cmd.add_argument(
        "-i",
        "--inspector",
        help="Show the GTK3 inspector.",
        action=BooleanOptionalAction,
    )

    cmd.add_argument(
        "-c",
        "--config",
        action="store",
        dest="config",
        help="Path to the config directory.",
        default=get_config_path(),
    )

    cmd.set_defaults(func=run)
