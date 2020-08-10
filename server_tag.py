#!/usr/bin/env python3

import sys
import iterm2
import subprocess

from server_config import product_server_map, test_server_map
from settings import product_tab_color, testing_tab_color, other_tab_color
from utils import get_ip_by_host


def get_host_config(host):
    host = get_ip_by_host(host)
    prod_name = product_server_map.get(host)
    test_name = test_server_map.get(host)

    if prod_name:  # product env config
        return prod_name, iterm2.Color(*product_tab_color)
    elif test_name:  # testing env config
        return test_name, iterm2.Color(*testing_tab_color)
    else:  # other env config
        return host, iterm2.Color(*other_tab_color)


async def main(connection):
    app = await iterm2.async_get_app(connection)
    session = app.current_terminal_window.current_tab.current_session
    change = iterm2.LocalWriteOnlyProfile()
    host = sys.argv[1].split('@')[-1]

    alias, color = get_host_config(host)

    change.set_badge_text(alias)
    change.set_tab_color(color)
    change.set_use_tab_color(True)
    await session.async_set_profile_properties(change)
    command = ['ssh'] + sys.argv[1:]
    subprocess.call(command)
    change.set_badge_text('')
    change.set_use_tab_color(False)
    await session.async_set_profile_properties(change)


iterm2.run_until_complete(main)
