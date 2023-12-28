import unittest

import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

from sora.widgets.label import Label, LabelProps
from sora.widgets.bind import Variable


LABEL = "SomeLabel"
JUSTIFY = Gtk.Justification.CENTER
WRAP = True
ANGLE = 90
XALIGN = 0.8
YALIGN = 0.2

class TestBaseWidget(unittest.TestCase):
    def test_init_with_defaults(self):
        label = Label(LabelProps())

        self.assertFalse(label.get_label())
    
        pass
