from sora.config.config import Config
from sora.config.styling import parse_style_sheet

from gi.repository import Gtk, Gdk


class App:
    """
    The main application.
    """

    def __init__(
        self,
        config: Config,
    ):
        """
        Creates a new App.

        :param config: The config to use.
        """

        self.config = config

        self.__load_styles()

        for window in config.windows:
            window.show()

    def __load_styles(self):
        """
        Loads the styles.
        """

        if css := parse_style_sheet(self.config.path):
            css_provider = Gtk.CssProvider()
            css_provider.load_from_data(css.encode())
            context = Gtk.StyleContext()
            screen = Gdk.Screen.get_default()
            context.add_provider_for_screen(
                screen, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
            )

    def run(self):
        """
        Runs the application.
        """

        Gtk.main()
