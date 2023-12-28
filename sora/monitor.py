from gi.repository import Gdk


class Monitor:
    """
    Represents a monitor connected to the system.
    """

    def __init__(self, name: str, x: int, y: int, width: int, height: int) -> None:
        """
        Creates a new monitor.

        :param name: The name of the monitor.
        :param x: The x coordinate of the monitor.
        :param y: The y coordinate of the monitor.
        :param width: The width of the monitor.
        :param height: The height of the monitor.
        """

        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    @staticmethod
    def from_gdk_monitor(gdk_monitor: Gdk.Monitor | None):
        """
        Creates a new monitor from a Gdk.Monitor.

        :param gdk_monitor: The Gdk.Monitor to create the monitor from.
        :return: The created monitor or None.
        """

        if gdk_monitor:
            geometry = gdk_monitor.get_geometry()
            return Monitor(
                name=gdk_monitor.get_model() or "",
                x=geometry.x,
                y=geometry.y,
                width=geometry.width,
                height=geometry.height,
            )


def get_monitor(identifier: str | int):
    """
    Gets a monitor by its name or index.

    :param identifier: The name or index of the monitor.
    :return: The monitor or None.
    """

    display = Gdk.Display.get_default()

    if not display:
        return None

    if type(identifier) is int:
        return Monitor.from_gdk_monitor(display.get_monitor(identifier))

    for i in range(display.get_n_monitors()):
        monitor = display.get_monitor(i)
        if monitor and monitor.get_model() == identifier:
            return Monitor.from_gdk_monitor(monitor)


def list_monitors():
    """
    Lists all monitors connected to the system.

    :return: A list of monitors.
    """

    display = Gdk.Display.get_default()
    if not display:
        return []

    monitors: list[Monitor] = []
    for i in range(display.get_n_monitors()):
        monitors.append(Monitor.from_gdk_monitor(display.get_monitor(i)))

    return monitors


def get_primary_monitor():
    """
    Gets the primary monitor.

    :return: The primary monitor.
    """

    display = Gdk.Display.get_default()
    return Monitor.from_gdk_monitor(display.get_primary_monitor())
