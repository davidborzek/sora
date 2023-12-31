from dataclasses import dataclass
from sora.widgets.base import BaseWidget, BaseWidgetProps

from gi.repository import Gtk, GObject

from sora.widgets.bind import Bindable


@dataclass(kw_only=True)
class StackProps(BaseWidgetProps):
    transition_type: Bindable[Gtk.StackTransitionType] = Gtk.StackTransitionType.NONE
    items: Bindable[dict[Gtk.Widget]] | None = None
    visible_child_name: Bindable[str] | None = None


class Stack(BaseWidget(Gtk.Stack), Gtk.Stack):
    __items: dict[str, Gtk.Widget] = {}

    def __init__(self, props: StackProps):
        super().__init__(props)
        self._bind_property("transition_type", props.transition_type)
        self._bind_property("items", props.items)
        self._bind_property("visible_child_name", props.visible_child_name)

    @GObject.Property(type=GObject.TYPE_PYOBJECT)
    def items(self):
        return self.__items

    @items.setter
    def items(self, items: dict[str, Gtk.Widget]):
        for current in self.get_children():
            current.destroy()

        for name, widget in items.items():
            self.add_titled(widget, name, name)

        self.__items = items
