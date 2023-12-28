from enum import Enum
from gi.repository import Gtk, Gdk
from sora.geometry import Geometry
from sora.monitor import get_monitor, get_primary_monitor


class WindowType(Enum):
    """
    The type of a window.
    """

    DOCK = 1
    NORMAL = 2
    DIALOG = 3
    TOOLBAR = 4
    UTILITY = 5
    DESKTOP = 6
    NOTIFICATION = 7

    def to_gdk_window_type_hint(self):
        """
        Converts the window type to a Gdk.WindowTypeHint.
        """

        match self:
            case WindowType.DOCK:
                return Gdk.WindowTypeHint.DOCK
            case WindowType.NORMAL:
                return Gdk.WindowTypeHint.NORMAL
            case WindowType.DIALOG:
                return Gdk.WindowTypeHint.DIALOG
            case WindowType.TOOLBAR:
                return Gdk.WindowTypeHint.TOOLBAR
            case WindowType.UTILITY:
                return Gdk.WindowTypeHint.UTILITY
            case WindowType.DESKTOP:
                return Gdk.WindowTypeHint.DESKTOP
            case WindowType.NOTIFICATION:
                return Gdk.WindowTypeHint.NOTIFICATION


class Window(Gtk.Window):
    """
    A window that can be placed on a monitor.
    """

    def __init__(
        self,
        name: str,
        widget: Gtk.Widget,
        monitor: str | int | None = None,
        wm_ignore: bool = False,
        window_type: WindowType = WindowType.DOCK,
        geometry: Geometry = Geometry(),
    ):
        """
        Creates a new Window.

        :param name: The name of the window.
        :param widget: The widget to display.
        :param monitor: The monitor to display the window on.
        :param wm_ignore: Whether the window manager should ignore (reserve space for) the window.
        :param window_type: The type of the window.
        :param geometry: The geometry of the window.
        """

        super().__init__(
            name=name,
            title=name,
            type=Gtk.WindowType.POPUP if wm_ignore else Gtk.WindowType.TOPLEVEL,
            decorated=False,
            skip_taskbar_hint=True,
            skip_pager_hint=True,
            type_hint=window_type.to_gdk_window_type_hint(),
            resizable=False,
            window_position=Gtk.WindowPosition.NONE,
            gravity=Gdk.Gravity.CENTER,
        )

        self.stick()
        self.set_keep_above(True)

        monitor_obj = get_monitor(monitor) if monitor else get_primary_monitor()
        if not monitor_obj:
            raise LookupError("could not get monitor")

        self.set_default_size(
            geometry.size.x.to_pixel_relative(monitor_obj.width),
            geometry.size.y.to_pixel_relative(monitor_obj.height),
        )

        self.move(
            monitor_obj.x + geometry.offset.x.to_pixel_relative(monitor_obj.width),
            monitor_obj.y + geometry.offset.y.to_pixel_relative(monitor_obj.height),
        )

        self.add(widget)
