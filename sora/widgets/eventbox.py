from dataclasses import dataclass
from enum import Enum
from typing import Callable

from gi.repository import Gtk, GObject, Gdk

from sora.widgets.base import BaseWidget, BaseWidgetProps


class ScrollDirection(Enum):
    """
    The direction of a scroll event.
    """

    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4


@dataclass(kw_only=True)
class EventBoxProps(BaseWidgetProps):
    """
    Properties for the EventBox widget.

    :param child: The child of the event box.
    :param on_hover: The function to call when the mouse enters the event box.
    :param on_hover_lost: The function to call when the mouse leaves the event box.
    :param on_scroll: The function to call when the mouse is scrolled.
    :param on_click: The function to call when the event box is clicked.
    :param on_middle_click: The function to call when the event box is middle clicked.
    :param on_right_click: The function to call when the event box is right clicked.
    """

    child: Gtk.Widget
    on_hover: Callable[[], None] | None = None
    on_hover_lost: Callable[[], None] | None = None
    on_scroll: Callable[[ScrollDirection], None] | None = None
    on_click: Callable[[], None] | None = None
    on_middle_click: Callable[[], None] | None = None
    on_right_click: Callable[[], None] | None = None


class EventBox(BaseWidget(Gtk.EventBox), Gtk.EventBox):
    """
    A EventBox that can be hovered, scrolled and clicked.
    """

    _on_hover: Callable[[], None] | None = None
    _on_hover_lost: Callable[[], None] | None = None
    _on_scroll: Callable[[ScrollDirection], None] | None = None
    __on_click: Callable[[], None] | None = None
    __on_middle_click: Callable[[], None] | None = None
    __on_right_click: Callable[[], None] | None = None

    def __init__(self, props: EventBoxProps):
        """
        Creates a new EventBox.

        :param props: The properties of the event box.
        """

        super().__init__(props)

        if self._on_hover:
            self.add_events(Gdk.EventMask.ENTER_NOTIFY_MASK)
            self.connect("enter-notify-event", lambda *_: self._on_hover())

        if self._on_hover_lost:
            self.add_events(Gdk.EventMask.LEAVE_NOTIFY_MASK)
            self.connect("leave-notify-event", lambda *_: self._on_hover_lost())

        if self._on_scroll:
            self.add_events(Gdk.EventMask.SCROLL_MASK)
            self.add_events(Gdk.EventMask.SMOOTH_SCROLL_MASK)

            self.connect("scroll-event", self.__on_scroll)

        if self.__on_click or self.__on_middle_click or self.__on_right_click:
            self.connect("button-press-event", self.__handle_on_click)

        self.connect("enter-notify-event", self.__set_css_hover)
        self.connect("leave-notify-event", self.__unset_css_hover)
        self.connect("button-press-event", self.__set_css_active)
        self.connect("button-release-event", self.__unset_css_active)

    @GObject.Property(type=GObject.TYPE_PYOBJECT)
    def child(self) -> Gtk.Widget:
        """
        The child of the event box.
        """

        return self.get_child()

    @child.setter
    def child(self, child: Gtk.Widget):
        """
        Sets the child of the event box.
        """

        for current in self.get_children():
            current.destroy()

        self.add(child)

    @GObject.Property(type=GObject.TYPE_PYOBJECT)
    def on_hover(self) -> Callable[[], None] | None:
        """
        The function to call when the mouse enters the event box.
        """

        return self._on_hover

    @on_hover.setter
    def on_hover(self, on_hover: Callable[[], None] | None):
        """
        Sets the function to call when the mouse enters the event box.
        """

        self._on_hover = on_hover

    @GObject.Property(type=GObject.TYPE_PYOBJECT)
    def on_hover_lost(self) -> Callable[[], None] | None:
        """
        The function to call when the mouse leaves the event box.
        """

        return self._on_hover_lost

    @on_hover_lost.setter
    def on_hover_lost(self, on_hover_lost: Callable[[], None] | None):
        """
        Sets the function to call when the mouse leaves the event box.
        """

        self._on_hover_lost = on_hover_lost

    @GObject.Property(type=GObject.TYPE_PYOBJECT)
    def on_scroll(self) -> Callable[[ScrollDirection], None] | None:
        """
        The function to call when the mouse is scrolled.
        """

        return self._on_scroll

    @on_scroll.setter
    def on_scroll(self, on_scroll: Callable[[ScrollDirection], None] | None):
        """
        Sets the function to call when the mouse is scrolled.
        """

        self._on_scroll = on_scroll

    @GObject.Property(type=GObject.TYPE_PYOBJECT)
    def on_click(self):
        """
        The function to call when the event box is clicked.
        """

        return self.__on_click

    @on_click.setter
    def on_click(self, on_click: Callable[[], None] | None = None):
        """
        Sets the function to call when the event box is clicked.
        """

        self.__on_click = on_click

    @GObject.Property(type=GObject.TYPE_PYOBJECT)
    def on_middle_click(self):
        """
        The function to call when the event box is middle clicked.
        """

        return self.__on_middle_click

    @on_middle_click.setter
    def on_middle_click(self, on_middle_click: Callable[[], None] | None = None):
        """
        Sets the function to call when the event box is middle clicked.
        """

        self.__on_middle_click = on_middle_click

    @GObject.Property(type=GObject.TYPE_PYOBJECT)
    def on_right_click(self):
        """
        The function to call when the event box is right clicked.
        """

        return self.__on_right_click

    @on_right_click.setter
    def on_right_click(self, on_right_click: Callable[[], None] | None = None):
        """
        Sets the function to call when the event box is right clicked.
        """

        self.__on_right_click = on_right_click

    def __handle_on_click(self, _, event: Gdk.EventButton):
        """
        Handles a click event.

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

    def __on_scroll(self, _, event: Gdk.EventScroll):
        """
        Handles a scroll event.

        :param _: The widget (unused).
        :param event: The event.
        """

        (_, x, y) = event.get_scroll_deltas()
        if y < 0:
            self._on_scroll(ScrollDirection.UP)
        elif y > 0:
            self._on_scroll(ScrollDirection.DOWN)

        if x > 0:
            self._on_scroll(ScrollDirection.RIGHT)
        elif x < 0:
            self._on_scroll(ScrollDirection.LEFT)

    def __set_css_hover(self, widget: Gtk.EventBox, _):
        """
        Sets the :hover CSS class for the hover state.
        """

        widget.set_state_flags(Gtk.StateFlags.PRELIGHT, False)

    def __unset_css_hover(self, widget: Gtk.EventBox, _):
        """
        Removes the :hover CSS class for the hover state.
        """

        widget.unset_state_flags(Gtk.StateFlags.PRELIGHT)

    def __set_css_active(self, widget: Gtk.EventBox, _):
        """
        Sets the :active CSS class for the active state.
        """

        widget.set_state_flags(Gtk.StateFlags.ACTIVE, False)

    def __unset_css_active(self, widget: Gtk.EventBox, _):
        """
        Removes the :active CSS class for the active state.
        """

        widget.unset_state_flags(Gtk.StateFlags.ACTIVE)
