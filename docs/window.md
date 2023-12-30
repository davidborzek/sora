## Window

A window defines a window on the screen, which can contain a single widget.

**Properties**

| Property      | Type                        | Description                                                                                                    |
| ------------- | --------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `name`        | `str`                       | The name of the window.                                                                                        |
| `widget`      | `str`                       | The widget to display in the window.                                                                           |
| `monitor`     | `int` or `str`              | The monitor to display the window on. This can be either the index of the monitor, or the name of the monitor. |
| `wm_ignore`   | `bool`                      | Whether the window manager should ignore (reserve space for) the window.                                       |
| `geometry`    | [`Geometry`](#geometry)     | The geometry of the window.                                                                                    |
| `window_type` | [`WindowType`](#windowtype) | The type of the window.                                                                                        |

**Example**

```python
from sora.window import Window, WindowType
from sora.geometry import Geometry
from sora.widgets.label import Label, LabelProps

window = Window(
    name="My Window",
    widget=Label(LabelProps(label="Hello, world!")),
    monitor=0,
    wm_ignore=True,
    geometry=Geometry(x="50%", y="50%", width="100px", height="100px"),
    window_type=WindowType.DOCK,
)
```

## Geometry

The geometry of a window.

**Properties**

| Property | Type  | Description                   |
| -------- | ----- | ----------------------------- |
| `x`      | `str` | The x position of the window. |
| `y`      | `str` | The y position of the window. |
| `width`  | `str` | The width of the window.      |
| `height` | `str` | The height of the window.     |

> Note: The values of the geometry properties are strings, because they can be either absolute values (e.g. `100px`) or relative values (e.g. `50%`).

## WindowType

The type of a window. This specifies [`_NET_WM_WINDOW_TYPE`](https://specifications.freedesktop.org/wm-spec/1.3/ar01s05.html) on X11.

- `DOCK`
- `NORMAL`
- `DIALOG`
- `TOOLBAR`
- `UTILITY`
- `DESKTOP`
- `NOTIFICATION`
