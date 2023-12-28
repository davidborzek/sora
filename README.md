# sora

sora is an experimental widget system, extendable and configurable using python and based on GTK3.
You can create your own widgets in any window manager.

It is heavily inspired by some existing widget systems and window managers, see [Credits](#credits).

> Note: sora is still in development, and not ready for production use.
> You should expect breaking changes for the configuration api.
> Currently only x11 is supported.

# Configuration

sora is configured using python, and the configuration file is located at `$XDG_CONFIG_HOME/sora/config.py`. (usually `~/.config/sora/config.py`)

You can specify the config directory using `-c` flag.

## Quick start

```python
from sora.widgets.label import Label, LabelProps
from sora.window import Window
from sora.geometry import Geometry

# Create a new label widget.
label = Label(
    LabelProps(label="Hello, world!", classnames=["label"]),
)

# Create a new window with the label widget.
window = Window(
    name="Bar",
    monitor=0,
    widget=label,
    geometry=Geometry(
        height="30px",
        width="100%",
    ),
)

# Export the window, so sora can use it.
# Exported windows are visible by default.
windows = [window]
```

## Styling

sora uses [GTK CSS](https://docs.gtk.org/gtk3/css-overview.html) for styling. You can style your widgets using either [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) or [Sass](https://sass-lang.com/).
GTK CSS is similar to Vanilla CSS, but does not support all CSS Properties.
Checkout the [Supported CSS Properties](https://docs.gtk.org/gtk3/css-properties.html) for more information.

The styles are loaded from the config directory, and sora looks for a `style.scss` or `style.css` file.

### GTK Debugger

You can use the GTK Debugger to inspect the widgets and their properties.

To start sora with the GTK Debugger, use the `--inspector` flag.

```bash
$ sora --inspector
```

# Development

## Requirements

- python3
- gtk3
- libsass

## Running locally

```bash
$ ./bin/sora -c .config/
```

> Note: You should create a local config directory at `.config/` for development.
> Otherwise, sora will use the default config directory at `$XDG_CONFIG_HOME/sora`.

# Credits

- [eww](https://github.com/elkowar/eww)
- [ags](https://github.com/Aylur/ags)
- [awesomewm](https://github.com/awesomeWM/awesome)
- [qtile](https://github.com/qtile/qtile)
