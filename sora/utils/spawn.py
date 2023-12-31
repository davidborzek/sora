import logging
import re
from typing import Callable
from gi.repository import GLib, Gio


def subprocess(
    cmd: list[str] | str,
    callback: Callable[[str], None],
):
    """
    Starts a subprocess and calls the callback for each line of stdout.

    :param cmd: The command to run.
    :param callback: The callback to call for each line of stdout.
    :return: The subprocess.
    """

    try:
        if type(cmd) is str:
            cmd = re.split(r"\s+", cmd)

        process = Gio.Subprocess.new(
            cmd,
            Gio.SubprocessFlags.STDOUT_PIPE | Gio.SubprocessFlags.STDERR_PIPE,
        )

        if not process:
            raise Exception("failed to start subprocess: process is None")

        def read(stdout: Gio.DataInputStream):
            def cb(stream: Gio.DataInputStream, res):
                if stream:
                    (output, _) = stream.read_line_finish_utf8(res)
                    if type(output) is str:
                        callback(output)
                        read(stream)

            stdout.read_line_async(GLib.PRIORITY_LOW, None, cb)

        pipe = process.get_stdout_pipe()
        if not pipe:
            raise Exception("failed to start subprocess: stdout is None")

        stdout = Gio.DataInputStream(
            base_stream=pipe,
            close_base_stream=True,
        )

        read(stdout)

        process.wait_async(
            None,
            lambda *_: logging.info(
                f"Subprocess finished with exit code {process.get_exit_status()}"
            ),
        )

        return process
    except Exception as e:
        raise Exception(f"failed to start subprocess {e}")
