import gi

gi.require_version("Gdk", "3.0")

import unittest
from unittest.mock import MagicMock

from gi.repository import Gdk

from sora.monitor import Monitor, get_monitor, get_primary_monitor, list_monitors

NUMERIC_MONITOR_IDENTIFIER = 1
MONITOR_NAME = "TestMonitor"
X = 600
Y = 700
WIDTH = 1920
HEIGHT = 1080


def mock_gdk_monitor(model, x, y, height, width):
    geometry = Gdk.Rectangle()
    geometry.x = x
    geometry.y = y
    geometry.height = height
    geometry.width = width

    monitor = MagicMock()
    monitor.get_model = MagicMock(return_value=model)
    monitor.get_geometry = MagicMock(return_value=geometry)

    return monitor


class TestMonitor(unittest.TestCase):
    def test_from_gdk_monitor(self):
        gdk_monitor = mock_gdk_monitor(MONITOR_NAME, X, Y, HEIGHT, WIDTH)

        monitor = Monitor.from_gdk_monitor(gdk_monitor)

        self.assertEqual(monitor.name, MONITOR_NAME)
        self.assertEqual(monitor.x, X)
        self.assertEqual(monitor.y, Y)
        self.assertEqual(monitor.height, HEIGHT)
        self.assertEqual(monitor.width, WIDTH)

    def test_from_gdk_monitor_return_none(self):
        monitor = Monitor.from_gdk_monitor(None)
        self.assertIsNone(monitor)


class TestGetMonitor(unittest.TestCase):
    def test_returns_none_when_display_is_none(self):
        Gdk.Display.get_default = MagicMock(return_value=None)

        monitor = get_monitor(NUMERIC_MONITOR_IDENTIFIER)
        self.assertIsNone(monitor, Monitor)

        Gdk.Display.get_default.assert_called_once()

    def test_returns_monitor_for_numeric_identifier(self):
        display_mock = MagicMock()
        display_mock.get_monitor = MagicMock(return_value=MagicMock())

        Gdk.Display.get_default = MagicMock(return_value=display_mock)

        monitor = get_monitor(NUMERIC_MONITOR_IDENTIFIER)
        self.assertIsInstance(monitor, Monitor)

        Gdk.Display.get_default.assert_called_once()
        display_mock.get_monitor.assert_called_once_with(NUMERIC_MONITOR_IDENTIFIER)

    def test_returns_monitor_with_monitor_name(self):
        mock_monitor = mock_gdk_monitor(MONITOR_NAME, 0, 0, 0, 0)
        display_mock = MagicMock()
        display_mock.get_n_monitors = MagicMock(return_value=1)
        display_mock.get_monitor = MagicMock(return_value=mock_monitor)

        Gdk.Display.get_default = MagicMock(return_value=display_mock)

        monitor = get_monitor(MONITOR_NAME)
        self.assertIsInstance(monitor, Monitor)

        Gdk.Display.get_default.assert_called_once()
        display_mock.get_n_monitors.assert_called_once()
        display_mock.get_monitor.assert_called_once_with(0)


class TestListMonitors(unittest.TestCase):
    def test_returns_empty_array_when_display_is_none(self):
        Gdk.Display.get_default = MagicMock(return_value=None)
        monitors = list_monitors()

        self.assertFalse(monitors)
        Gdk.Display.get_default.assert_called_once()

    def test_returns_monitor_list(self):
        display_mock = MagicMock()
        display_mock.get_n_monitors = MagicMock(return_value=2)
        display_mock.get_monitor = MagicMock(return_value=MagicMock())

        Gdk.Display.get_default = MagicMock(return_value=display_mock)
        monitors = list_monitors()

        self.assertTrue(monitors)
        self.assertEqual(len(monitors), 2)
        self.assertIsInstance(monitors[0], Monitor)
        self.assertIsInstance(monitors[1], Monitor)

        Gdk.Display.get_default.assert_called_once()
        display_mock.get_n_monitors.assert_called_once()

        self.assertEqual(display_mock.get_monitor.call_count, 2)


class TestGetPrimaryMonitor(unittest.TestCase):
    def test_returns_primary_monitor(self):
        display_mock = MagicMock()
        Gdk.Display.get_default = MagicMock(return_value=display_mock)

        monitor = get_primary_monitor()
        self.assertIsInstance(monitor, Monitor)

        Gdk.Display.get_default.assert_called_once()
        display_mock.get_primary_monitor.assert_called_once()

    def test_returns_none(self):
        display_mock = MagicMock()
        display_mock.get_primary_monitor = MagicMock(return_value=None)
        Gdk.Display.get_default = MagicMock(return_value=display_mock)

        monitor = get_primary_monitor()
        self.assertIsNone(monitor)

        Gdk.Display.get_default.assert_called_once()
        display_mock.get_primary_monitor.assert_called_once()


if __name__ == "__main__":
    unittest.main()
