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

## Button

A button widget.

**Properties**

| Property          | Type                 | Description                                                    |
| ----------------- | -------------------- | -------------------------------------------------------------- |
| `label`           | `str`                | The label of the button.                                       |
| `on_click`        | `Callable[[], None]` | The callback that is called when the button is clicked.        |
| `on_middle_click` | `Callable[[], None]` | The callback that is called when the button is middle clicked. |
| `on_right_click`  | `Callable[[], None]` | The callback that is called when the button is right clicked.  |

## CenterBox

A box that must contain exactly three children, which will be placed at the start, center and end of the box.

**Properties**

| Property | Type                                                                                               | Description                  |
| -------- | -------------------------------------------------------------------------------------------------- | ---------------------------- |
| `start`  | [`Gtk.Widget`](https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Widget.html#Gtk.Widget) | The start child of the box.  |
| `center` | [`Gtk.Widget`](https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Widget.html#Gtk.Widget) | The center child of the box. |
| `end`    | [`Gtk.Widget`](https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Widget.html#Gtk.Widget) | The end child of the box.    |

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
