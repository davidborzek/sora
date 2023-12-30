# Configuration

sora is configured using python and the configuration file is located at `$XDG_CONFIG_HOME/sora/config.py`. (usually `~/.config/sora/config.py`)

You can specify the config directory using the `-c` flag.

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

Follow this wiki page for more information about the configuration API.
