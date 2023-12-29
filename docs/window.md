## Window

A window defines a window on the screen, which can contain a single widget.

### Properties

- `name`: `str`: The name of the window.
- `widget`: `str`: The widget to display in the window.
- `monitor`: `int | str`: The monitor to display the window on. This can be either the index of the monitor, or the name of the monitor.
- `wm_ignore`: `bool`: Whether the window manager should ignore (reserve space for) the window.
- `geometry`: `Geometry`: The geometry of the window.
- `window_type`: `WindowType`: The type of the window.

## Geometry

The geometry of a window.

### Properties

- x: `str`: The x position of the window.
- y: `str`: The y position of the window.
- width: `str`: The width of the window.
- height: `str`: The height of the window.

> Note: The values of the geometry properties are strings, because they can be either absolute values (e.g. `100px`) or relative values (e.g. `50%`).

## WindowType

The type of a window. This specifies `_NET_WM_WINDOW_TYPE` on X11.

### Types

- `DOCK`
- `NORMAL`
- `DIALOG`
- `TOOLBAR`
- `UTILITY`
- `DESKTOP`
- `NOTIFICATION`
