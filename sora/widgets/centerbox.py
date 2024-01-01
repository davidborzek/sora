from dataclasses import dataclass
from gi.repository import Gtk, GObject

from sora.widgets.base import BaseWidget, BaseWidgetProps
from sora.service import Bindable


@dataclass(kw_only=True)
class CenterBoxProps(BaseWidgetProps):
    """
    Properties for the CenterBox widget.

    :param orientation: The orientation of the box.
    :param children: The children of the box.
    """

    children: tuple[Gtk.Widget, Gtk.Widget, Gtk.Widget]
    orientation: Bindable[Gtk.Orientation] = Gtk.Orientation.HORIZONTAL


class CenterBox(BaseWidget(Gtk.Box), Gtk.Box):
    """
    A box that must contain three widgets: left, center, right.
    """

    def __init__(self, props: CenterBoxProps):
        """
        Creates a new CenterBox.

        :param props: The properties of the box.
        """

        super().__init__(props)
        self._bind_property("children", props.children)
        self._bind_property("orientation", props.orientation)

    @GObject.Property(type=GObject.TYPE_PYOBJECT)
    def children(self) -> tuple[Gtk.Widget, Gtk.Widget, Gtk.Widget]:
        """
        The children of the box.
        """

        return self.get_children()

    @children.setter
    def children(self, children: tuple[Gtk.Widget, Gtk.Widget, Gtk.Widget]):
        """
        Sets the children of the box.
        """

        for current in self.get_children():
            current.destroy()

        (left, center, right) = children
        self.pack_start(left, True, True, 0)
        self.set_center_widget(center)
        self.pack_end(right, True, True, 0)
