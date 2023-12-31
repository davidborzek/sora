from dataclasses import dataclass
import logging
from sora.widgets.base import BaseWidget, BaseWidgetProps

from gi.repository import Gtk, GObject

from sora.widgets.bind import Bindable


@dataclass(kw_only=True)
class StackProps(BaseWidgetProps):
    transition_type: Bindable[Gtk.StackTransitionType] = Gtk.StackTransitionType.NONE
    items: Bindable[dict[Gtk.Widget]] | None = None
    visible_child_name: Bindable[str] | None = None
    vhomogeneous: Bindable[bool] = True
    hhomogeneous: Bindable[bool] = True


class Stack(BaseWidget(Gtk.Stack), Gtk.Stack):
    __items: dict[str, Gtk.Widget] = {}

    def __init__(self, props: StackProps):
        super().__init__(props)
        self._bind_property("transition_type", props.transition_type)
        self._bind_property("items", props.items)
        self._bind_property("visible_child_name", props.visible_child_name)
        self._bind_property("vhomogeneous", props.vhomogeneous)
        self._bind_property("hhomogeneous", props.hhomogeneous)

    @GObject.Property(type=GObject.TYPE_PYOBJECT)
    def items(self):
        return self.__items

    @items.setter
    def items(self, items: dict[str, Gtk.Widget]):
        for current in self.get_children():
            current.destroy()

        for name, widget in items.items():
            self.add_named(widget, name)

        self.__items = items

    def add_named(self, child: Gtk.Widget, name: str):
        if name in self.__items:
            logging.error(f"child with name {name} already in stack.")
            return

        self.__items[name] = child
        super().add_named(child, name)
