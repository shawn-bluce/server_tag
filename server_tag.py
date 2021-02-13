#!/usr/bin/env python3

import sys
import subprocess

from utils import get_ip_by_host, color_text
from settings import default_tab_color

try:
    import iterm2
    from server_config import get_server_list
except (ModuleNotFoundError, ImportError) as e:
    color_text.error(e)
    exit()


def get_host_config(host: str) -> tuple:
    """
    :param host: domain or ip or ssh_config
    :return: tuple(host_name, iterm2_color)
    """
    ip_addr = get_ip_by_host(host)
    for server in get_server_list():
        if ip_addr == server.host:
            return server.name, server.color
    return host, default_tab_color


async def main(connection):
    app = await iterm2.async_get_app(connection)
    session = app.current_terminal_window.current_tab.current_session
    change = iterm2.LocalWriteOnlyProfile()
    host = sys.argv[1].split('@')[-1]

    alias, color = get_host_config(host)

    # set config
    change.set_badge_text(alias)
    change.set_tab_color(color)
    change.set_use_tab_color(True)
    change.set_badge_color(color)

    # apply new config for iterm2 and ssh to server
    await session.async_set_profile_properties(change)
    command = ['ssh'] + sys.argv[1:]
    subprocess.call(command)

    # revert config
    change.set_badge_text('')
    change.set_use_tab_color(False)
    await session.async_set_profile_properties(change)


if __name__ == '__main__':
    iterm2.run_until_complete(main)
