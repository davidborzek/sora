from dataclasses import dataclass
from typing import Callable

from gi.repository import GObject, Gtk, Gdk

from sora.widgets.base import BaseWidget, BaseWidgetProps
from sora.widgets.bind import Bindable


@dataclass(kw_only=True)
class ButtonProps(BaseWidgetProps):
    """
    Properties for the Button widget.

    :param label: The label of the button.
    :param on_click: The function to call when the button is clicked.
    :param on_middle_click: The function to call when the button is middle clicked.
    :param on_right_click: The function to call when the button is right clicked.
    """

    label: Bindable[str] | None = None
    on_click: Callable[[], None] | None = None
    on_middle_click: Callable[[], None] | None = None
    on_right_click: Callable[[], None] | None = None


class Button(BaseWidget(Gtk.Button), Gtk.Button):
    """
    A button that can be clicked.
    """

    __on_click: Callable[[], None] | None = None
    __on_middle_click: Callable[[], None] | None = None
    __on_right_click: Callable[[], None] | None = None

    def __init__(self, props: ButtonProps):
        """
        Creates a new Button.

        :param props: The properties of the button.
        """

        super().__init__(props)
        self._bind_property("label", props.label)
        self._bind_property("on_click", props.on_click)
        self._bind_property("on_middle_click", props.on_middle_click)
        self._bind_property("on_right_click", props.on_right_click)

        self.connect("button-press-event", self.__handle_on_click)

    @GObject.Property(type=GObject.TYPE_PYOBJECT)
    def on_click(self):
        """
        The function to call when the button is clicked.
        """

        return self.__on_click

    @on_click.setter
    def on_click(self, on_click: Callable[[], None] | None = None):
        """
        Sets the function to call when the button is clicked.
        """

        self.__on_click = on_click

    @GObject.Property(type=GObject.TYPE_PYOBJECT)
    def on_middle_click(self):
        """
        The function to call when the button is middle clicked.
        """

        return self.__on_middle_click

    @on_middle_click.setter
    def on_middle_click(self, on_middle_click: Callable[[], None] | None = None):
        """
        Sets the function to call when the button is middle clicked.
        """

        self.__on_middle_click = on_middle_click

    @GObject.Property(type=GObject.TYPE_PYOBJECT)
    def on_right_click(self):
        """
        The function to call when the button is right clicked.
        """

        return self.__on_right_click

    @on_right_click.setter
    def on_right_click(self, on_right_click: Callable[[], None] | None = None):
        """
        Sets the function to call when the button is right clicked.
        """

        self.__on_right_click = on_right_click

    def __handle_on_click(self, _, event: Gdk.EventButton):
        """
        Handles the on click event.

        :param _: The widget (unused).
        :param event: The event.
        """

        match event.button:
            case 1 if self.on_click:
                self.on_click()
            case 2 if self.on_middle_click:
                self.on_middle_click()
            case 3 if self.on_right_click:
                self.on_right_click()
