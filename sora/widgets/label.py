from dataclasses import dataclass
from sora.widgets.base import BaseWidget, BaseWidgetProps

from gi.repository import Gtk

from sora.widgets.bind import Bindable


@dataclass(kw_only=True)
class LabelProps(BaseWidgetProps):
    """
    Properties for the Label widget.

    :param label: The label of the label.
    :param justify: The justification of the label.
    :param wrap: Whether the label wraps.
    :param angle: The angle of the label.
    :param xalign: The horizontal alignment of the label.
    :param yalign: The vertical alignment of the label.
    """

    # TODO: char limit and truncation
    # TODO: maybe pango markup
    label: Bindable[str] | None = None
    justify: Bindable[Gtk.Justification] = Gtk.Justification.LEFT
    wrap: Bindable[bool] = False
    angle: Bindable[float] = 0
    xalign: Bindable[float] = 0.5
    yalign: Bindable[float] = 0.5


class Label(BaseWidget(Gtk.Label), Gtk.Label):
    """
    A label that can display text.
    """

    def __init__(self, props: LabelProps):
        """
        Creates a new Label.

        :param props: The properties of the label.
        """

        super().__init__(props)
        self._bind_property("label", props.label)
        self._bind_property("justify", props.justify)
        self._bind_property("wrap", props.wrap)
        self._bind_property("angle", props.angle)
        self._bind_property("xalign", props.xalign)
        self._bind_property("yalign", props.yalign)
