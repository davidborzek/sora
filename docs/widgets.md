# Widgets

## Base

All widgets inherit from the base widget class. So the following properties are available for all widgets.

**Properties**

| Property       | Type                                                                         | Description                                                                                                                         |
| -------------- | ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `name`         | `str`                                                                        | The name of the widget.                                                                                                             |
| `visible`      | `bool`                                                                       | Whether the widget is visible or not.                                                                                               |
| `tooltip_text` | `str`                                                                        | The tooltip text of the widget.                                                                                                     |
| `valign`       | [`Gtk.Align`](https://lazka.github.io/pgi-docs/Gtk-3.0/enums.html#Gtk.Align) | The vertical alignment of the widget.                                                                                               |
| `halign`       | [`Gtk.Align`](https://lazka.github.io/pgi-docs/Gtk-3.0/enums.html#Gtk.Align) | The horizontal alignment of the widget.                                                                                             |
| `vexpand`      | `bool`                                                                       | Whether the widget should expand vertically or not.                                                                                 |
| `hexpand`      | `bool`                                                                       | Whether the widget should expand horizontally or not.                                                                               |
| `sensitive`    | `bool`                                                                       | Whether the widget is sensitive or not.                                                                                             |
| `classnames`   | `list[str]`, `str`                                                           | CSS class names of the widget.                                                                                                      |
| `cursor`       | `Cursor`                                                                     | The cursor of the widget. This only works for widgets that receives hover events (e.g. [EventBox](#eventbox) or [Button](#button)). |

## Box

A layout container that can contain multiple widgets.

**Properties**

| Property      | Type                                                                                                     | Description                                   |
| ------------- | -------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| `spacing`     | `int`                                                                                                    | The spacing between widgets.                  |
| `orientation` | [`Gtk.Orientation`](https://lazka.github.io/pgi-docs/Gtk-3.0/enums.html#Gtk.Orientation)                 | The orientation of the box.                   |
| `homogeneous` | `bool`                                                                                                   | Whether the box should be homogeneous or not. |
| `children`    | [`list[Gtk.Widget]`](https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Widget.html#Gtk.Widget) | The children of the box.                      |

**Example**

```python
from sora.widgets.box import Box, BoxProps
from gi.repository import Gtk

box = Box(
    BoxProps(
        spacing=10,
        orientation=Gtk.Orientation.VERTICAL,
        homogeneous=True,
        children=[
            # Add other widgets here.
        ],
    ),
)
```

## Button

A button widget.

**Properties**

| Property          | Type                 | Description                                                    |
| ----------------- | -------------------- | -------------------------------------------------------------- |
| `label`           | `str`                | The label of the button.                                       |
| `on_click`        | `Callable[[], None]` | The callback that is called when the button is clicked.        |
| `on_middle_click` | `Callable[[], None]` | The callback that is called when the button is middle clicked. |
| `on_right_click`  | `Callable[[], None]` | The callback that is called when the button is right clicked.  |

**Example**

```python
from sora.widgets.button import Button, ButtonProps

button = Button(
    ButtonProps(
        label="Click me!",
        on_click=lambda: print("Clicked!"),
        on_middle_click=lambda: print("Middle clicked!"),
        on_right_click=lambda: print("Right clicked!"),
    ),
)
```

## CenterBox

A box that must contain exactly three children, which will be placed at the start, center and end of the box.

**Properties**

| Property | Type                                                                                               | Description                  |
| -------- | -------------------------------------------------------------------------------------------------- | ---------------------------- |
| `start`  | [`Gtk.Widget`](https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Widget.html#Gtk.Widget) | The start child of the box.  |
| `center` | [`Gtk.Widget`](https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Widget.html#Gtk.Widget) | The center child of the box. |
| `end`    | [`Gtk.Widget`](https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Widget.html#Gtk.Widget) | The end child of the box.    |

**Example**

```python
from sora.widgets.centerbox import CenterBox, CenterBoxProps

centerbox = CenterBox(
    CenterBoxProps(
        start=Label(LabelProps(label="Start")),
        center=Label(LabelProps(label="Center")),
        end=Label(LabelProps(label="End")),
    ),
)
```

## EventBox

A widget that can receive events and must contain exactly one child.

**Properties**

| Property          | Type                                                                                               | Description                                                       |
| ----------------- | -------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| `child`           | [`Gtk.Widget`](https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Widget.html#Gtk.Widget) | The child of the event box.                                       |
| `on_hover`        | `Callable[[], None]`                                                                               | The callback that is called when the event box is hovered.        |
| `on_hover_lost`   | `Callable[[], None]`                                                                               | The callback that is called when the event box is unhovered.      |
| `on_scroll`       | `Callable[[ScrollDirection], None]`                                                                | The callback that is called when the event box is scrolled.       |
| `on_click`        | `Callable[[], None]`                                                                               | The callback that is called when the event box is clicked.        |
| `on_middle_click` | `Callable[[], None]`                                                                               | The callback that is called when the event box is middle clicked. |
| `on_right_click`  | `Callable[[], None]`                                                                               | The callback that is called when the event box is right clicked.  |

> Note: Supports `:hover` and `:active` CSS pseudo classes.

**Example**

```python
from sora.widgets.eventbox import EventBox, EventBoxProps

eventbox = EventBox(
    EventBoxProps(
        child=Label(LabelProps(label="Hover or click me!")),
        on_hover=lambda: print("Hovered!"),
        on_hover_lost=lambda: print("Unhovered!"),
        on_scroll=lambda direction: print(f"Scrolled {direction}!"),
        on_click=lambda: print("Clicked!"),
        on_middle_click=lambda: print("Middle clicked!"),
        on_right_click=lambda: print("Right clicked!"),
    ),
)
```

### ScrollDirection

The direction of a scroll event.

- `UP`
- `DOWN`
- `LEFT`
- `RIGHT`

## Label

A label widget.

**Properties**

| Property  | Type                                                                                         | Description                            |
| --------- | -------------------------------------------------------------------------------------------- | -------------------------------------- |
| `label`   | `str`                                                                                        | The text of the label.                 |
| `justify` | [`Gtk.Justification`](https://lazka.github.io/pgi-docs/Gtk-3.0/enums.html#Gtk.Justification) | The justification of the label.        |
| `wrap`    | `bool`                                                                                       | Whether the label should wrap or not.  |
| `angle`   | `float`                                                                                      | The angle of the label.                |
| `xalign`  | `float`                                                                                      | The horizontal alignment of the label. |
| `yalign`  | `float`                                                                                      | The vertical alignment of the label.   |

**Example**

```python
from sora.widgets.label import Label, LabelProps
from gi.repository import Gtk

label = Label(
    LabelProps(
        label="Hello, world!",
        justify=Gtk.Justification.CENTER,
        wrap=True,
        angle=45,
        xalign=0.5,
        yalign=0.5,
    ),
)
```

## Revealer

A widget that can reveal its child.

**Properties**

| Property              | Type                                                                                                           | Description                                     |
| --------------------- | -------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| `reveal_child`        | `bool`                                                                                                         | Whether the child is revealed or not.           |
| `transition_duration` | `int`                                                                                                          | The duration of the transition in milliseconds. |
| `transition_type`     | [`Gtk.RevealerTransitionType`](https://lazka.github.io/pgi-docs/Gtk-3.0/enums.html#Gtk.RevealerTransitionType) | The type of the transition.                     |
| `child`               | [`Gtk.Widget`](https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Widget.html#Gtk.Widget)             | The child of the revealer.                      |

**Example**

```python
from sora.widgets.revealer import Revealer, RevealerProps

revealer = Revealer(
    RevealerProps(
        reveal_child=True,
        transition_duration=500,
        transition_type=Gtk.RevealerTransitionType.CROSSFADE,
        child=Label(LabelProps(label="Hello, world!")),
    ),
)
```

## Slider

A slider widget.

**Properties**

| Property       | Type                                                                                     | Description                                                   |
| -------------- | ---------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| `orientation`  | [`Gtk.Orientation`](https://lazka.github.io/pgi-docs/Gtk-3.0/enums.html#Gtk.Orientation) | The orientation of the slider.                                |
| `inverted`     | `bool`                                                                                   | Whether the slider is inverted.                               |
| `max`          | `float`                                                                                  | The maximum value of the slider.                              |
| `min`          | `float`                                                                                  | The minimum value of the slider.                              |
| `step`         | `float`                                                                                  | The step of the slider.                                       |
| `value`        | `float`                                                                                  | The value of the slider.                                      |
| `draw_value`   | `bool`                                                                                   | Whether the value is drawn.                                   |
| `round_digits` | `int`                                                                                    | The number of digits to round to.                             |
| `marks`        | `list[list[tuple[float, Gtk.PositionType, str]]]`                                        | The marks of the slider.                                      |
| `scrollable`   | `bool`                                                                                   | Whether the slider is scrollable.                             |
| `on_change`    | `Callable[[float], None]`                                                                | The callback that is called when the slider value is changed. |

**Example**

```python
from sora.widgets.slider import Slider, SliderProps
from gi.repository import Gtk

slider = Slider(
    SliderProps(
        orientation=Gtk.Orientation.VERTICAL,
        inverted=True,
        max=100,
        min=0,
        step=1,
        value=50,
        draw_value=True,
        round_digits=0,
        marks=[
            [
                (0, Gtk.PositionType.TOP, "0"),
                (50, Gtk.PositionType.TOP, "50"),
                (100, Gtk.PositionType.TOP, "100"),
            ]
        ],
        scrollable=True,
        on_change=lambda value: print(f"Value changed to {value}!"),
    ),
)
```
