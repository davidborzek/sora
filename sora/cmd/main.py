import argparse
import sys

from sora.cmd import start


def main():
    main_parser = argparse.ArgumentParser(
        prog="sora", description="sora is an experimental widget system, extendable and configurable using python and based on GTK3."
    )

    main_parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="0.1.0",
    )

    subparsers = main_parser.add_subparsers()
    start.subcommand(subparsers)

    help_cmd = subparsers.add_parser("help", help="Print help and exit.")
    help_cmd.set_defaults(func=lambda _: main_parser.print_help())

    options = main_parser.parse_args()
    if func := getattr(options, "func", None):
        func(options)
    else:
        main_parser.print_usage()
        sys.exit(1)


if __name__ == "__main__":
    main()
