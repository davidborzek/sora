import unittest

import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

from sora.variable import Variable
from sora.widgets.base import BaseWidget, BaseWidgetProps
from sora.widgets.cursor import Cursor

NAME = "SomeName"
VISIBLE = False
TOOLTIP_TEXT = "SomeTooltipText"
VALIGN = Gtk.Align.CENTER
HALIGN = Gtk.Align.START
HEXPAND = True
VEXPAND = True
SENSITIVE = False
CURSOR = Cursor.POINTER
CLASSNAMES = ["class-a", "class-b"]

NEW_NAME = "NewName"
NEW_VISIBLE = True
NEW_TOOLTIP_TEXT = "NewTooltipText"
NEW_VALIGN = Gtk.Align.END
NEW_HALIGN = Gtk.Align.CENTER
NEW_HEXPAND = False
NEW_VEXPAND = False
NEW_SENSITIVE = True
NEW_CURSOR = Cursor.CROSSHAIR
NEW_CLASSNAMES = ["class-c", "class-d"]


class TestBaseWidget(unittest.TestCase):
    def test_init_with_defaults(self):
        widget = BaseWidget(Gtk.Label)(BaseWidgetProps())

        self.assertTrue(widget.get_name())
        self.assertTrue(widget.get_visible())
        self.assertFalse(widget.get_tooltip_text())
        self.assertEqual(widget.get_valign(), Gtk.Align.FILL)
        self.assertEqual(widget.get_halign(), Gtk.Align.FILL)
        self.assertFalse(widget.get_hexpand())
        self.assertFalse(widget.get_vexpand())
        self.assertTrue(widget.get_sensitive())
        self.assertFalse(widget.classnames)
        self.assertEqual(widget.cursor, Cursor.DEFAULT)

    def test_init(self):
        widget = BaseWidget(Gtk.Label)(
            BaseWidgetProps(
                name=NAME,
                visible=VISIBLE,
                tooltip_text=TOOLTIP_TEXT,
                valign=VALIGN,
                halign=HALIGN,
                hexpand=HEXPAND,
                vexpand=VEXPAND,
                sensitive=SENSITIVE,
                classnames=CLASSNAMES,
                cursor=CURSOR,
            )
        )

        self.assertEqual(widget.get_name(), NAME)
        self.assertFalse(widget.get_visible())
        self.assertEqual(widget.get_tooltip_text(), TOOLTIP_TEXT)
        self.assertEqual(widget.get_valign(), VALIGN)
        self.assertEqual(widget.get_halign(), HALIGN)
        self.assertTrue(widget.get_hexpand())
        self.assertTrue(widget.get_vexpand())
        self.assertFalse(widget.get_sensitive())
        self.assertEqual(widget.classnames, CLASSNAMES)
        self.assertEqual(widget.cursor, CURSOR)

    def test_init_binds(self):
        props = BaseWidgetProps(
            name=Variable(NAME),
            visible=Variable(VISIBLE),
            tooltip_text=Variable(TOOLTIP_TEXT),
            valign=Variable(VALIGN),
            halign=Variable(HALIGN),
            hexpand=Variable(HEXPAND),
            vexpand=Variable(VEXPAND),
            sensitive=Variable(SENSITIVE),
            classnames=Variable(CLASSNAMES),
            cursor=Variable(CURSOR),
        )

        widget = BaseWidget(Gtk.Label)(props)

        self.assertEqual(widget.get_name(), NAME)
        self.assertFalse(widget.get_visible())
        self.assertEqual(widget.get_tooltip_text(), TOOLTIP_TEXT)
        self.assertEqual(widget.get_valign(), VALIGN)
        self.assertEqual(widget.get_halign(), HALIGN)
        self.assertTrue(widget.get_hexpand())
        self.assertTrue(widget.get_vexpand())
        self.assertFalse(widget.get_sensitive())
        self.assertEqual(widget.classnames, CLASSNAMES)
        self.assertEqual(widget.cursor, CURSOR)

        props.name.value = NEW_NAME
        props.visible.value = NEW_NAME
        props.tooltip_text.value = NEW_TOOLTIP_TEXT
        props.valign.value = NEW_VALIGN
        props.halign.value = NEW_HALIGN
        props.hexpand.value = NEW_HEXPAND
        props.vexpand.value = NEW_VEXPAND
        props.sensitive.value = NEW_SENSITIVE
        props.classnames.value = NEW_CLASSNAMES
        props.cursor.value = NEW_CURSOR

        # after the notify signal, we can quit the main loop
        widget.connect("notify", lambda *_: Gtk.main_quit())
        Gtk.main()

        self.assertEqual(widget.get_name(), NEW_NAME)
        self.assertTrue(widget.get_visible())
        self.assertEqual(widget.get_tooltip_text(), NEW_TOOLTIP_TEXT)
        self.assertEqual(widget.get_valign(), NEW_VALIGN)
        self.assertEqual(widget.get_halign(), NEW_HALIGN)
        self.assertFalse(widget.get_hexpand())
        self.assertFalse(widget.get_vexpand())
        self.assertTrue(widget.get_sensitive())
        self.assertEqual(widget.classnames, NEW_CLASSNAMES)
        self.assertEqual(widget.cursor, NEW_CURSOR)


if __name__ == "__main__":
    unittest.main()
