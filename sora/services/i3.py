import threading
from dataclasses import dataclass
from gi.repository import GObject

from i3ipc import Connection, Event, WorkspaceReply

from sora.service import Service


@dataclass(kw_only=True)
class i3Workspace:
    """
    Represents an i3 workspace.

    :param num: The number of the workspace.
    :param name: The name of the workspace.
    :param visible: Whether the workspace is visible.
    :param focused: Whether the workspace is focused.
    :param urgent: Whether the workspace is urgent.
    """

    num: int
    name: str
    visible: bool
    focused: bool
    urgent: bool

    @classmethod
    def from_workspace_reply(cls, workspace: WorkspaceReply):
        """
        Creates a new i3Workspace from a WorkspaceReply.

        :param workspace: The WorkspaceReply to create the i3Workspace from.
        :return: The new i3Workspace.
        """

        return cls(
            num=workspace.num,
            name=workspace.name,
            visible=workspace.visible,
            focused=workspace.focused,
            urgent=workspace.urgent,
        )


class _i3(Service):
    __thread: threading.Thread
    __i3 = Connection(auto_reconnect=True)

    __workspaces: list[i3Workspace]

    def __init__(self):
        super().__init__()

        self.__get_workspaces()

        self.__thread = threading.Thread(target=self.__start_listeners)
        self.__thread.daemon = True
        self.__thread.start()

    def __start_listeners(self):
        self.__i3.on(Event.WORKSPACE, self.__on_workspace_change)
        self.__i3.main()

    def __on_workspace_change(self, *_):
        self.__get_workspaces()

    def __get_workspaces(self):
        workspaces = self.__i3.get_workspaces()
        workspaces.sort(key=lambda x: x.num)

        self.__workspaces = [i3Workspace.from_workspace_reply(ws) for ws in workspaces]
        self.notify("workspaces")

    @GObject.Property(type=GObject.TYPE_PYOBJECT)
    def workspaces(self):
        return self.__workspaces

    def command(self, cmd: str):
        """
        Sends a command to i3.

        :param cmd: The command to send.
        """
        self.__i3.command(cmd)


__instance: _i3 | None = None


def i3():
    """
    Gets the i3 connection.

    :return: The i3 connection.
    """
    global __instance

    if __instance is None:
        __instance = _i3()

    return __instance
