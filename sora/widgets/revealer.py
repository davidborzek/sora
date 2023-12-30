from dataclasses import dataclass

from sora.widgets.base import BaseWidget, BaseWidgetProps
from sora.widgets.bind import Bindable

from gi.repository import Gtk


@dataclass(kw_only=True)
class RevealerProps(BaseWidgetProps):
    """
    Properties for the Revealer widget.

    :param reveal_child: Whether the child is revealed.
    :param transition_duration: The duration of the transition in milliseconds.
    :param transition_type: The type of the transition animation.
    :param child: The child widget.
    """

    reveal_child: Bindable[bool] = False
    transition_duration: Bindable[int] = 1000
    transition_type: Bindable[
        Gtk.RevealerTransitionType
    ] = Gtk.RevealerTransitionType.NONE
    child: Bindable[Gtk.Widget] | None = None


class Revealer(BaseWidget(Gtk.Revealer), Gtk.Revealer):
    def __init__(self, props: RevealerProps):
        super().__init__(props)

        self._bind_property("reveal_child", props.reveal_child)
        self._bind_property("transition_duration", props.transition_duration)
        self._bind_property("transition_type", props.transition_type)
        self._bind_property("child", props.child)
