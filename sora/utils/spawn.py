from typing import Callable
from gi.repository import GLib, Gio


def subprocess(cmd: list[str], callback: Callable[[str], None]):
    def read(stdout: Gio.DataInputStream):
        def cb(stream: Gio.DataInputStream, res):
            if stream:
                (output, _) = stream.read_line_finish_utf8(res)
                if type(output) is str:
                    callback(output)
                    read(stream)

            pass

        stdout.read_line_async(GLib.PRIORITY_LOW, None, cb)

    process = Gio.Subprocess.new(
        cmd,
        Gio.SubprocessFlags.STDOUT_PIPE | Gio.SubprocessFlags.STDERR_PIPE,
    )

    if not process:
        return

    pipe = process.get_stdout_pipe()
    stdout = Gio.DataInputStream.new(pipe)

    read(stdout)

    return process
