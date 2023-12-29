from dataclasses import dataclass, fields
import re
from gi.repository import Gtk, GObject, Gdk
from sora.widgets.bind import Bindable, Variable
from sora.widgets.cursor import Cursor


@dataclass(kw_only=True)
class BaseWidgetProps:
    """
    Base properties for all widgets.

    :param name: The name of the widget.
    :param visible: Whether the widget is visible.
    :param tooltip_text: The tooltip text of the widget.
    :param valign: The vertical alignment of the widget.
    :param halign: The horizontal alignment of the widget.
    :param hexpand: Whether the widget expands horizontally.
    :param vexpand: Whether the widget expands vertically.
    :param sensitive: Whether the widget is sensitive.
    :param classnames: The classnames of the widget.
    :param cursor: The cursor of the widget.
    """

    # Gtk.Widget properties
    name: Bindable[str] | None = None
    visible: Bindable[bool] = True
    tooltip_text: Bindable[str] | None = None
    valign: Bindable[Gtk.Align] = Gtk.Align.FILL
    halign: Bindable[Gtk.Align] = Gtk.Align.FILL
    hexpand: Bindable[bool] = False
    vexpand: Bindable[bool] = False
    sensitive: Bindable[bool] = True

    # TODO: width and height

    # Custom Properties
    classnames: Bindable[list[str] | str] | None = None
    cursor: Bindable[Cursor] = Cursor.DEFAULT


def BaseWidget(Widget: type[Gtk.Widget]):
    """
    Returns the BaseWidget class for a given Gtk.Widget type (e.g. Gtk.Button).

    :param Widget: The Gtk.Widget type to create the BaseWidget for.
    :return: The BaseWidget class.
    """

    class _Widget(Widget):
        """
        Base widget for all widgets.
        """

        __cursor: str

        def __init__(self, props: BaseWidgetProps):
            """
            Creates a new BaseWidget.

            :param props: The properties of the widget.
            """

            super().__init__()

            # TODO: refactor me
            for field in fields(props):
                value = getattr(props, field.name)
                if value is not None and self.find_property(field.name):
                    if isinstance(value, Variable):
                        value.bind(self, field.name)
                        value = value.value

                    self.set_property(field.name, value)

            if not self.cursor == Cursor.DEFAULT:
                self.add_events(Gdk.EventMask.ENTER_NOTIFY_MASK)
                self.add_events(Gdk.EventMask.LEAVE_NOTIFY_MASK)

                self.connect("enter-notify-event", self.__set_cursor_on_hover)
                self.connect("leave-notify-event", self.__unset_cursor_on_hover)

        @GObject.Property(type=GObject.TYPE_PYOBJECT)
        def classnames(self) -> list[str]:
            """
            The classnames of the widget.
            """

            return self.get_style_context().list_classes() or []

        @classnames.setter
        def classnames(self, classnames: list[str] | str):
            """
            Sets the classnames of the widget.
            """

            if type(classnames) is str:
                classnames = re.split(" +", classnames.strip())

            style_context = self.get_style_context()
            for classname in style_context.list_classes():
                style_context.remove_class(classname)

            for classname in classnames:
                style_context.add_class(classname)

        @GObject.Property(type=str)
        def cursor(self):
            """
            The cursor of the widget.
            """

            return Cursor(self.__cursor)

        @cursor.setter
        def cursor(self, cursor: Cursor):
            """
            Sets the cursor of the widget.
            """

            self.__cursor = cursor

        def __set_cursor_on_hover(self, *_):
            """
            Sets the cursor on hover.
            """

            display = Gdk.Display.get_default()
            window = self.get_window()
            if display and window:
                window.set_cursor(Gdk.Cursor.new_from_name(display, self.__cursor))

        def __unset_cursor_on_hover(self, *_):
            """
            Unsets the cursor on hover.
            """

            window = self.get_window()
            if window:
                window.set_cursor(None)

    return _Widget
