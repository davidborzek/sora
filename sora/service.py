from typing import Any, Callable, TypeVar

from gi.repository import GObject, GLib


class Binding:
    _src: GObject.GObject
    _src_prop: str
    _map_fn: Callable[[Any], Any] | None = None

    def __init__(self, gobject: GObject.GObject, prop: str) -> None:
        self._src = gobject
        self._src_prop = prop

    def map(self, fn: Callable[[Any], Any]):
        """
        Sets the map function.

        :param fn: The map function.
        :return: The binding.
        """

        self._map_fn = fn
        return self

    def __get_value(self):
        value = self._src.get_property(self._src_prop)
        if self._map_fn:
            value = self._map_fn(value)
        return value

    def bind(self, target: GObject.GObject, prop: str):
        """
        Binds the binding to the given GObject property.

        :param target: The target GObject to bind to.
        :param prop: The property to bind to.
        """

        def on(*_):
            GLib.idle_add(target.set_property, prop, self.__get_value())

        target.set_property(prop, self.__get_value())
        self._src.connect(f"notify::{self._src_prop}", on)


class Service(GObject.GObject):
    def bind(
        self,
        prop: str,
    ):
        """
        Creates a new binding of a service property.

        :param prop: The property to bind to.
        """

        return Binding(self, prop)


T = TypeVar("T")

Bindable = T | Binding
"""
A bindable value. This can be either a value or a binding.
"""
