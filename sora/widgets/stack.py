from dataclasses import dataclass
import logging
from sora.widgets.base import BaseWidget, BaseWidgetProps

from gi.repository import Gtk, GObject
from sora.service import Bindable


@dataclass(kw_only=True)
class StackProps(BaseWidgetProps):
    """
    Properties for the Stack widget.

    :param transition_type: The type of transition to use when changing the visible child of the stack.
    :param items: A dictionary of child widgets to add to the stack.
    :param visible_child_name: The name of the visible child of the stack.
    :param vhomogeneous: Whether the stack should distribute the available space evenly among its children.
    :param hhomogeneous: Whether the stack should distribute the available space evenly among its children.
    """

    transition_type: Bindable[Gtk.StackTransitionType] = Gtk.StackTransitionType.NONE
    transition_duration: Bindable[int] = 200
    items: Bindable[dict[Gtk.Widget]] | None = None
    visible_child_name: Bindable[str] | None = None
    vhomogeneous: Bindable[bool] = True
    hhomogeneous: Bindable[bool] = True


class Stack(BaseWidget(Gtk.Stack), Gtk.Stack):
    """
    A widget that shows a single child at a time.
    """

    __items: dict[str, Gtk.Widget] = {}

    def __init__(self, props: StackProps):
        """
        Create a new Stack widget.

        :param props: The properties for the Stack widget.
        """

        super().__init__(props)
        self._bind_property("transition_type", props.transition_type)
        self._bind_property("transition_duration", props.transition_duration)
        self._bind_property("items", props.items)
        self._bind_property("visible_child_name", props.visible_child_name)
        self._bind_property("vhomogeneous", props.vhomogeneous)
        self._bind_property("hhomogeneous", props.hhomogeneous)

    @GObject.Property(type=GObject.TYPE_PYOBJECT)
    def items(self):
        """
        The items in the stack.
        """

        return self.__items

    @items.setter
    def items(self, items: dict[str, Gtk.Widget]):
        """
        Set the items in the stack.

        :param items: The items to set.
        """

        for current in self.get_children():
            current.destroy()

        for name, widget in items.items():
            self.add_named(widget, name)

        self.__items = items

    def add_named(self, child: Gtk.Widget, name: str):
        """
        Add a child to the stack.

        :param child: The child to add.
        :param name: The name of the child.
        """

        if name in self.__items:
            logging.error(f"child with name {name} already in stack.")
            return

        self.__items[name] = child
        super().add_named(child, name)
