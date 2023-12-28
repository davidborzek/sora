from pathlib import Path
import sass
import re
import os


def parse_scss(scss: str):
    """
    Parses a SCSS string to CSS.

    :param scss: The SCSS string to parse.
    :return: The parsed CSS string.
    """

    return sass.compile(string=scss)


def __replace_env(content: str) -> str:
    """
    Replaces all environment variables in the given string.

    :param content: The string to replace the environment variables in.
    :return: The string with the replaced environment variables.
    """

    return re.sub("env\((.+)\)", lambda v: os.getenv(v.group(1)), content)


def parse_style_sheet(path: Path):
    """
    Parses the style sheet at the given path.
    Either CSS or SCSS.

    :param path: The path to the style sheet.
    :return: The parsed style sheet.
    """

    css_file = path.joinpath("style.css")
    scss_file = path.joinpath("style.scss")

    if css_file.exists() and scss_file.exists():
        raise Exception(
            "Both SCSS and CSS file exists. Only one of the should exists at a time."
        )

    if css_file.exists():
        with open(css_file, "r", encoding="utf-8") as file:
            css = file.read()

        return __replace_env(css)
    elif scss_file.exists():
        with open(scss_file, "r", encoding="utf-8") as file:
            scss = file.read()

        scss = __replace_env(scss)
        return parse_scss(scss)

    return None
