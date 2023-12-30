from dataclasses import dataclass
from sora.widgets.base import BaseWidget, BaseWidgetProps
from gi.repository import Gtk, GObject

from sora.widgets.bind import Bindable


@dataclass(kw_only=True)
class BoxProps(BaseWidgetProps):
    """
    Properties for the Box widget.

    :param orientation: The orientation of the box.
    :param spacing: The spacing between the children.
    :param homogeneous: Whether the box is homogeneous.
    :param children: The children of the box.
    """

    orientation: Bindable[Gtk.Orientation] = Gtk.Orientation.HORIZONTAL
    spacing: Bindable[int] = 0
    homogeneous: Bindable[bool] = True
    children: Bindable[list[Gtk.Widget]] | None = None


class Box(BaseWidget(Gtk.Box), Gtk.Box):
    """
    A box that can contain other widgets.
    """

    def __init__(self, props: BoxProps):
        """
        Creates a new Box.

        :param props: The properties of the box.
        """

        super().__init__(props)
        self._bind_property("orientation", props.orientation)
        self._bind_property("spacing", props.spacing)
        self._bind_property("homogeneous", props.homogeneous)
        self._bind_property("children", props.children)

    @GObject.Property(type=GObject.TYPE_PYOBJECT)
    def children(self) -> list[Gtk.Widget]:
        """
        The children of the box.
        """

        return self.get_children()

    @children.setter
    def children(self, children: list[Gtk.Widget]):
        """
        Sets the children of the box.

        :param children: The children to set.
        """

        for current in self.get_children():
            current.destroy()
        for new in children:
            self.add(new)
