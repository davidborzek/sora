from dataclasses import dataclass
from typing import Callable
from sora.widgets.base import BaseWidget, BaseWidgetProps
from gi.repository import Gtk, GObject, Gdk

from sora.service import Bindable


@dataclass(kw_only=True)
class SliderProps(BaseWidgetProps):
    """
    Properties for the Slider widget.

    :param orientation: The orientation of the slider.
    :param inverted: Whether the slider is inverted.
    :param min: The minimum value of the slider.
    :param max: The maximum value of the slider.
    :param step: The step of the slider.
    :param value: The value of the slider.
    :param draw_value: Whether the value of the slider is drawn.
    :param round_digits: The number of digits to round the value to.
    :param marks: The marks of the slider.
    :param scrollable: Whether the slider is scrollable.
    :param on_change: The callback to call when the value of the slider changes.
    """

    orientation: Bindable[Gtk.Orientation] = Gtk.Orientation.HORIZONTAL
    inverted: Bindable[bool] = False
    min: Bindable[float] = 0
    max: Bindable[float] = 100
    step: Bindable[float] = 1
    value: Bindable[float] = 0
    draw_value: Bindable[bool] = True
    round_digits: Bindable[int] = 1
    marks: Bindable[list[tuple[float, Gtk.PositionType, str]]] | None = None
    scrollable: Bindable[bool] = True
    on_change: Callable[[float], None] | None = None


class Slider(BaseWidget(Gtk.Scale), Gtk.Scale):
    __on_change: Callable[[float], None] | None = None
    __marks: list[tuple[float, Gtk.PositionType, str]] = []
    __scrollable: bool = True

    """
    A slider widget.
    """

    def __init__(self, props: SliderProps):
        """
        Creates a new Slider.

        :param props: The properties of the slider.
        """

        super().__init__(props)
        self._bind_property("orientation", props.orientation)
        self._bind_property("inverted", props.inverted)
        self._bind_property("min", props.min)
        self._bind_property("max", props.max)
        self._bind_property("step", props.step)
        self._bind_property("value", props.value)
        self._bind_property("draw_value", props.draw_value)
        self._bind_property("round_digits", props.round_digits)
        self._bind_property("marks", props.marks)
        self._bind_property("scrollable", props.scrollable)
        self._bind_property("on_change", props.on_change)

        self.__on_change = props.on_change

        self.get_adjustment().connect("notify::value", self.__handle_on_change)

    def __handle_on_change(self, *_):
        if self.__on_change:
            self.__on_change(self.value)

    @GObject.Property(type=GObject.TYPE_FLOAT)
    def value(self) -> float:
        """
        The value of the slider.
        """

        return self.get_adjustment().get_value()

    @value.setter
    def value(self, value: float):
        """
        Sets the value of the slider.

        :param value: The value to set.
        """

        self.get_adjustment().set_value(value)

    @GObject.Property(type=GObject.TYPE_FLOAT)
    def min(self) -> float:
        """
        The minimum value of the slider.
        """

        return self.get_adjustment().get_lower()

    @min.setter
    def min(self, min: float):
        """
        Sets the minimum value of the slider.

        :param min: The minimum value to set.
        """

        self.get_adjustment().set_lower(min)

    @GObject.Property(type=GObject.TYPE_FLOAT)
    def max(self) -> float:
        """
        The maximum value of the slider.
        """

        return self.get_adjustment().get_upper()

    @max.setter
    def max(self, max: float):
        """
        Sets the maximum value of the slider.

        :param max: The maximum value to set.
        """

        self.get_adjustment().set_upper(max)

    @GObject.Property(type=GObject.TYPE_FLOAT)
    def step(self) -> float:
        """
        The step of the slider.
        """

        return self.get_adjustment().get_step_increment()

    @step.setter
    def step(self, step: float):
        """
        Sets the step of the slider.

        :param step: The step to set.
        """

        self.get_adjustment().set_step_increment(step)

    @GObject.Property(type=GObject.TYPE_PYOBJECT)
    def on_change(self) -> Callable[[float], None] | None:
        """
        The callback to call when the value of the slider changes.
        """

        return self.__on_change

    @on_change.setter
    def on_change(self, on_change: Callable[[float], None] | None):
        """
        Sets the callback to call when the value of the slider changes.

        :param on_change: The callback to set.
        """

        self.__on_change = on_change

    @GObject.Property(type=GObject.TYPE_PYOBJECT)
    def marks(self) -> list[tuple[float, Gtk.PositionType, str]]:
        """
        The marks of the slider.
        """

        return self.__marks

    @marks.setter
    def marks(self, marks: list[tuple[float, Gtk.PositionType, str]]):
        """
        Sets the marks of the slider.

        :param marks: The marks to set.
        """

        self.__marks = marks

        self.clear_marks()
        for mark in marks:
            self.add_mark(*mark)

    @GObject.Property(type=GObject.TYPE_BOOLEAN, default=True)
    def scrollable(self) -> bool:
        """
        Whether the slider is scrollable.
        """

        return self.__scrollable

    @scrollable.setter
    def scrollable(self, scrollable: bool):
        """
        Sets whether the slider is scrollable.

        :param scrollable: Whether the slider is scrollable.
        """

        self.__scrollable = scrollable

    def do_scroll_event(self, event: Gdk.EventScroll):
        if self.__scrollable:
            (_, x, y) = event.get_scroll_deltas()
            if y < 0 or x > 0:
                self.value += self.step
            elif y > 0 or x < 0:
                self.value -= self.step

        return Gtk.Scale.do_scroll_event(self, event)
