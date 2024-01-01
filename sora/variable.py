import logging
from typing import Callable, Generic, TypeVar

from gi.repository import GObject, GLib, Gio
from sora.service import Binding

from sora.utils.spawn import subprocess


T = TypeVar("T")


class Variable(Generic[T], GObject.GObject):
    """
    Variable that can be bound to a GObject property.
    """

    __value: T
    __interval_id: int | None = None
    __process: Gio.Subprocess | None = None

    def __init__(self, v: T) -> None:
        """
        Creates a new variable.

        :param v: The initial value.
        """

        super().__init__()
        self.__value = v

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

    @classmethod
    def listen(cls, cmd: list[str], initial: str = ""):
        """
        Creates a new variable that listens on a command output and updates itself.

        :param cmd: The listening command.
        :param initial: The initial value.
        :return: The created variable.
        """

        variable = cls(initial)

        def on_data(data: str):
            print(data)
            variable.value = data

        variable.__process = subprocess(cmd, on_data)
        return variable

    @GObject.Property(type=GObject.TYPE_PYOBJECT)
    def value(self):
        """
        The value of the variable.
        """

        return self.__value

    @value.setter
    def value(self, v: T):
        """
        Sets the value of the variable.
        """

        self.__value = v

    def bind(self):
        """
        Creates a new binding to the variable.
        """

        return Binding(self, "value")

    def stop_interval(self):
        """
        Stops the interval. When the interval is not running, nothing happens.
        """

        if self.__interval_id:
            GLib.source_remove(self.__interval_id)
            self.__interval_id = None
        else:
            logging.warn("Cannot stop interval: no interval running.")

    def stop_listener(self):
        """
        Stops the listener. When the listener is not running, nothing happens.
        """

        if self.__process:
            self.__process.force_exit()
            self.__process = None
        else:
            logging.warn("Cannot stop listener: no process running.")
