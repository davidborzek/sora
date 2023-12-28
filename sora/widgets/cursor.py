from enum import Enum


class Cursor(Enum):
    """
    Available cursors for the cursor property.
    """

    DEFAULT = "default"
    HELP = "help"
    POINTER = "pointer"
    CONTEXT_MENU = "context-menu"
    PROGRESS = "progress"
    WAIT = "wait"
    CELL = "cell"
    CROSSHAIR = "crosshair"
    TEXT = "text"
    VERTICAL_TEXT = "vertical-text"
    ALIAS = "alias"
    COPY = "copy"
    NO_DROP = "no-drop"
    MOVE = "move"
    NOT_ALLOWED = "not-allowed"
    GRAB = "grab"
    GRABBING = "grabbing"
    ALL_SCROLL = "all-scroll"
    COL_RESIZE = "col-resize"
    ROW_RESIZE = "row-resize"
    N_RESIZE = "n-resize"
    E_RESIZE = "e-resize"
    S_RESIZE = "s-resize"
    W_RESIZE = "w-resize"
    NE_RESIZE = "ne-resize"
    NW_RESIZE = "nw-resize"
    SW_RESIZE = "sw-resize"
    SE_RESIZE = "se-resize"
    EW_RESIZE = "ew-resize"
    NS_RESIZE = "ns-resize"
    NESW_RESIZE = "nesw-resize"
    NWSE_RESIZE = "nwse-resize"
    ZOOM_IN = "zoom-in"
    ZOOM_OUT = "zoom-out"

    def __str__(self):
        return str(self.value)
