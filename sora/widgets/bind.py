import logging
from typing import Any, Callable, Generic, TypeVar

from gi.repository import GObject, GLib

T = TypeVar("T")


class Variable(Generic[T], GObject.GObject):
    """
    Variable that can be bound to a GObject property.
    """

    __value: T
    __transform: Callable[[T], Any] | None = None
    __interval_id: int | None = None

    def __init__(self, v: T) -> None:
        """
        Creates a new variable.

        :param v: The initial value.
        """

        super().__init__()
        self.__value = v

    def transform(self, transform: Callable[[T], Any]):
        """
        Sets the transform function.

        :param transform: The transform function.
        :return: The variable.
        """

        self.__transform = transform
        return self

    @classmethod
    def interval(cls, interval, func: Callable[[], T]):
        """
        Creates a new variable that updates itself every interval seconds.

        :param interval: The interval in seconds.
        :param func: The function to get the value from.
        :return: The created variable.
        """

        variable = Variable(func())

        def on_timeout():
            variable.value = func()
            return GLib.SOURCE_CONTINUE

        variable.__interval_id = GLib.timeout_add_seconds(interval, on_timeout)
        return variable

    @GObject.Property(type=GObject.TYPE_PYOBJECT)
    def value(self):
        """
        The value of the variable.
        """

        if self.__transform:
            return self.__transform(self.__value)

        return self.__value

    @value.setter
    def value(self, v: T):
        """
        Sets the value of the variable.
        """

        self.__value = v

    def bind(self, object: GObject.GObject, prop: str):
        """
        Binds the variable to the given GObject property.

        :param object: The GObject to bind to.
        :param prop: The property to bind to.
        """

        self.connect("notify::value", lambda *_: self.__on_bind(object, prop))

    def __on_bind(self, object: GObject.GObject, prop: str):
        """
        Called when the variable has changed and the GObject property should be updated.
        """

        GLib.idle_add(object.set_property, prop, self.value)

    def stop_interval(self):
        """
        Stops the interval. When the interval is not running, nothing happens.
        """

        if self.__interval_id:
            GLib.source_remove(self.__interval_id)
        else:
            logging.warn("Cannot stop interval: no interval running.")


Bindable = T | Variable[T]
